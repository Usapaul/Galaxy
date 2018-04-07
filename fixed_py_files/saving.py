#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Получаемые аргументы: имя изображения без расширения
image=sys.argv[1]

comments_file=open(image+'comments.dat','r')
# В этом файле должны быть записаны строки вида "X Y {comment}"
# В словаре comments ключом будет кортеж (x,y)
comments={}
for line in comments_file:
	line=line.strip().split()
	comments[(float(line[0]),float(line[1]))]=' '.join(line[2:])
comments_file.close()

catalog=open(image+'field.cat','r')
# p хранит имена параметров(X, Y, A, B, APER и т.д.)
p=[]
# newcatalog -- это список из строк + комментарий в конце
newcatalog=[]
# Запоминаем номера столбцов X_IMAGE и Y_IMAGE.
# Номера параметров записаны между решеткой и названием.
# Вычитаем 1, так как нумерация столбцов в Python с нуля.
# Если присвоенные здесь значения (-1) не изменятся в теле
# цикла при чтении заголовка, то косяк где-то
xcolumn=-1
ycolumn=-1
for headline in catalog:
	headline=headline.split()
	if headline[0]=='#':
		p.append(headline[2])
		if headline[2]=='X_IMAGE':
			xcolumn=int(headline[1])-1
		if headline[2]=='Y_IMAGE':
			ycolumn=int(headline[1])-1
	else:
		if xcolumn==-1 or ycolumn==-1:
			raise SystemExit('STOP: X_IMAGE or Y_IMAGE is not found')
		np=len(p)
		if np!=len(headline):
			# нет, ну вдруг косяк какой-то в каталоге
			catalog.close()
			raise SystemExit('STOP: The number of received parameters ' \
							 'is not equal to the number ' \
							 'of parameters in the header')
		if np<1:
			catalog.close()
			raise SystemExit('STOP: No header in the catalog')
		# Добавлю указание, что в последнем столбе для каждого объекта
		# записан "мой_комментарий"
		p.append('MY_COMMENT')
		np+=1
		for xy_key in comments.keys():
			# Если разница в положениях совсем маленькая, порядка 
			# одного-двух пикселей, то считаем, что это один и 
			# тот же объект. Здесь я взял dx+dy < 4.0 pix
			delta_x=abs(float(headline[xcolumn])-float(xy_key[0]))
			delta_y=abs(float(headline[ycolumn])-float(xy_key[1]))
			if delta_x+delta_y<4.0:
				headline.append(comments[xy_key])
				newcatalog.append(headline)
				# Выходим из цикла, свянного с поиском в каталоге
				# объекта с указанными координатами. Нашли же!
				break
		# Выходим из цикла, где читается заголовок, так как сейчас уже
		# программа зашла в ветвление ELSE, а значит, заголовок прочли		
		break
else:
	# Нет, ну вдруг так получилось, что заголовок есть, а объектов нет:)
	raise SystemExit('STOP: No object is found')

# Заголовок считан, а также уже есть первая строка данных
# Теперь чтение продолжится отдельно, чтобы избежать излишних проверок
# на то, является ли строка заголовочной. Известно, что дальше 
# строки идут в одном формате, поэтому не проверяя просто их читаем
for line in catalog:
	line=line.strip().split()
	for xy_key in comments.keys():
		# Если разница в положениях совсем маленькая, порядка 
		# одного-двух пикселей, то считаем, что это один и 
		# тот же объект. Здесь я взял dx+dy < 4.0 pix
		delta_x=abs(float(line[xcolumn])-float(xy_key[0]))
		delta_y=abs(float(line[ycolumn])-float(xy_key[1]))
		if delta_x+delta_y<4.0:
			line.append(comments[xy_key])
			newcatalog.append(line)
			# Выходим из цикла, свянного с поиском в каталоге
			# объекта с указанными координатами. Нашли же!
			break
catalog.close()

def write_with_format(s):
	# Уширяет строку до длины number символов, заполняя пробелами слева
	number=11
	return s.rjust(number)

best=open(image+'best.dat','w')
# Записывается заголовочная строка, т.е. имя каждого столбца
line=list(map(write_with_format,p))
line=' '.join(line)
best.write(line+'\n')
# only 'ok' -- сперва записываем только ok, потом остальное
# хитрой конструкцией: два раза прогоняется тело цикла.
# В первом запись если srtarswith(ok)==True, во втором если False
for only_ok in True,False:
	for i in range(len(newcatalog)):
		if newcatalog[i][-1].startswith('ok') == only_ok:
			line=list(map(write_with_format,newcatalog[i][0:-1]))
			line=' '.join(line)+'  '+newcatalog[i][-1]
			best.write(line+'\n')
best.close()

