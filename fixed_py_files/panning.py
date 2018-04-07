#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# Получаемые аргументы: 
# --- название файла с изображением (например, "f160")
# без указания расширения. Нужен еще файл [image]aper.fits.
# --- индикатор (нужно просто листать или принимать комментарии)
# ,-- названия файлов с regions (.reg) или просто с координатами X Y 
# Файлов может быть сколько угодно
args=sys.argv[1:]
image=args[0]
indicator=int(args[1])
# indicator=0 соответствует запуску без записи комментариев
# indicator=1 соответствует запуску только для переключения
# между объектами посредством +/-
if indicator not in (0,1):
	raise SystemExit('Unknown indicator: '+str(indicator))
# В переменной regions будет храниться строка с повторяющимися
# "-region [namefile] ". Это нужно для загрузки regions вместе
# с запуском самого DS9
regions=''
# Просто если подали на вход не .reg, но файл содержит координаты, 
# а значит, можно с ним работать
extension_is_not_reg=False
for i in args[2:]:
	if i.endswith('.reg'):
		regions+='-region '+i+' '
	else:
		extension_is_not_reg=True
if len(regions)==0 and extension_is_not_reg==False:
	raise SystemExit('No region files specified')

def create_XYlist(files):
	# Производится получение списка координат regions, которые 
	# будут взяты из всех файлов files, и будет проверено, что
	# координаты различны, т.е. не отличаются всего на пару пикселей.
	# Список "уникальных" значений X Y потребуется дальше для 
	# перемещения по изображению с помощью команды pan.
	# Координаты X Y берутся из файлов [].reg.
	# Но могут быть файлы и с другим расширением, где записаны
	# только координаты без всяких "circle" и "color".
	xy=[]
	for file in files:
		f=open(file,'r')
		extension=file.split('.')[-1]
		if extension=='reg':
			line=f.readline().strip()
			while line!='image':
				# Предполагается, что файл с regions содержит последней
				# строкой заголовка только слово 'image', и больше 
				# в этой строке ничего не содержится, а после нее
				# идут уже записи с самими "регионами", где через
				# пробел записано все, и X и Y находятся на 
				# второй и третьей позициях в строке !через пробел все!
				line=f.readline().strip()

			for line in f:
				line=line.split()
				# Список xy хранит кортежи из координат (x,y).
				# Напоминаю самому себе, что в строке line сначала
				# записана форма региона (например, circle), а затем
				# через пробелы -- координаты X Y. Поэтому
				# line[0]='circle', line[1&2]= X & Y
				xy.append((float(line[1]),float(line[2])))
		else:
			# Для файлов без расширения .reg предполагается, что
			# в первых строках могут быть записаны комментарии, а
			# потом только координаты X Y (во всяком случае,
			# каждая строка с них начинается, не важно что в строке еще
			line=f.readline().strip()
			while line[0]=='#':
				line=f.readline().strip()
			line=line.split()
			xy.append((float(line[0]),float(line[1])))
			for line in f:
				line=line.split()
				xy.append((float(line[0]),float(line[1])))
		f.close()
	# В сортированном списке близкие друг к другу значения будут рядом,
	# поэтому с ними удобнее работать, чтобы в итоге сохранить только 
	# те, которые не повторяются
	xy.sort()
	xyclear=[]
	xyclear.append(xy[0])
	for i in range(1,len(xy)):
		# Если в отсортированном списке координат попадаются такие, что
		# сумма разностей по X и Y не превышает 2.0 (pix), то не будем
		# записывать такие, считая, что это один и тот же объект
		if abs(xy[i][0]-xy[i-1][0])+abs(xy[i][1]-xy[i-1][1])>2.0:
			xyclear.append(xy[i])
	# Функция, собственно, вернет список координат, чтобы дальше можно
	# было с ним работать
	return xyclear

coords=create_XYlist(args[2:])

# Вызывается ds9, как можно видеть, с желаемыми параметрами
command='ds9 '+image+'aper.fits '+regions
command+='-scale log -scale limits -0.002 2.0 '
command+=image+'.fits '+regions+'-cmap invert yes '
command+='-scale linear -scale limits -0.005 0.01 '+'&'
os.system(command)
print('DS9 is opening now...')
print()
waiting=input('Press Enter when DS9 is opened (not earlier)\n')
print()

def do_pan(indicator,xy):
	# Перемещение по изображению с использованием команды pan.
	# Координаты, куда перемещаться надо, записаны построчно (X,Y)
	# в списке xy. Так как команды ds9 вызываются через XPASET, нужно
	# убедиться (внутри ds9), что XPA включен.
	pan_command='xpaset -p ds9 pan to '
	frame_command='xpaset -p ds9 frame next '
	print('Number of objects:',len(xy))
	if indicator==1:
		# Если indicator=1, то будут приниматься комментарии с экрана
		print("Enter a comment for each selected object.")
		print("The following comment will be a good mark for a galaxy: 'ok'")
		print("And this is a bad mark: 'no'")
		print("Other comments will be saved too,")
		print("but objects with 'no' will be removed")
		print()
		# j -- номер текущего объекта
		j=0
		list_comments=[]
		# В файле [image]ok.dat будут сохранены координаты объектов 
		# с комментариями, которые будут читаться через stdin
		namefile=image+'comments.dat'
		f=open(namefile,'w')
		fokno=open(image+'allcom.dat','w')
		for coords in xy:
			j+=1
			counter=str(coords[0])+' '+str(coords[1])	
			counter+=' ('+str(j)+'/'+str(len(xy))+')'
			for i in 1,2:
				# Pan -- both frames
				os.system(pan_command+str(coords[0])+' '+str(coords[1]))
				os.system(frame_command)
			comment=input('Enter your comment for the object '+counter+'\n')
			if comment=='':
				comment='--'
			if comment not in ('no','No','NO'):
				# Комментарий 'no' означает, что данный объект не нужно
				# записывать вовсе. Если же комментарий другой, то
				# он будет записан вместе с координатами либо в 
				# список list_comments, который будет хранить только
				# комментарии, не начинающиеся с 'ok', либо сразу 
				# в файл -- потому что хочется, чтобы в начале 
				# файла были объекты с 'ok', а потом все остальные
				xy_string=str(coords[0]).rjust(9)+' '+str(coords[1]).rjust(9)
				if comment[0:2] not in ('ok','Ok','OK'):
					list_comments.append(xy_string+' '+comment+'\n')
				else:
					f.write(xy_string+' '+comment+'\n')
			# Все равно запишем все комментарии в файл {image}allcom.dat
			xy_string=str(coords[0]).rjust(9)+' '+str(coords[1]).rjust(9)
			fokno.write(xy_string+' '+comment+'\n')
		for line in list_comments:
			# Теперь запишем в файл все, что "не ok"
			f.write(line)
		f.close()
		fokno.close()
		print('Comments with X Y saved in file '+namefile)
	elif indicator==0:
		print("Enter +/- for panning to next/last object,")
		print("'note' or 'exit'")
		# Если indicator=0, то включается простое перемещение
		# от объекта к объекту с помощью ввода "+" или "-"
		# В переменной k содержится индекс текущего объекта из xy
		k=0
		n=len(xy)
		# Если мне захочется комментарий написать, то он запишется
		# в файл extracomments.dat, только нужно написать 'note'
		f=open('extracomments.dat','w')
		f.write('Extracomments for image '+image+'\n')
		what_to_do=''
		while what_to_do!='exit':
			for i in 1,2:
				# Pan -- both frames
				os.system(pan_command+str(xy[k][0])+' '+str(xy[k][1]))
				os.system(frame_command)
			print('Object:',xy[k][0],xy[k][1])
			what_to_do=input()
			while what_to_do not in ('+','-','exit','note'):
				what_to_do=input("Please enter +/-, 'note' or 'exit'\n")
			if what_to_do=='+':
				k=k%n+1
			elif what_to_do=='-':
				k=(k-1+n-1)%n+1
			elif what_to_do=='note':
				note=input('Type a note:\n')
				f.write(str(xy[k][0])+' '+str(xy[k][1])+' '+note+'\n')
		f.close()	
		print('All notes saved in file extracomments.dat')
	else:
		print('Unknown indicator: '+str(indicator))

do_pan(indicator,coords)

