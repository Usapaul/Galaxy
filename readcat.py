#!/usr/bin/env python
# -*- coding: utf-8 -*-

import regions 
import sys

# Получаемые аргументы: имя изображения без расширения
image=sys.argv[1]

# xell хранит значение параметра эллиптичности.
# Объекты с ellipticity<xell не интересуют/не сохраняются
xell=0.60
catalog=open(image+'field.cat','r')
# p хранит имена параметров(X, Y, A, B, APER и т.д.)
p=[]
# data хранит значения параметров для каждого объекта 
data={}
for headline in catalog:
	headline=headline.split()
	if headline[0]=='#':
		p.append(headline[2])
		if p[0]!='NUMBER':
			raise SystemExit('STOP: NUMBER must be on the 1st line')
		# Запоминаем номер ellcolumn столбца с параметром эллиптичности.
		# Номера параметров записаны между решеткой и названием. 
		# Вычитаем 1, так как нумерация столбцов в Python с нуля.
		if headline[2]=='ELLIPTICITY':
			ellcolumn=int(headline[1])-1
	else:
		def checkdata(p):
		# Функция checkdata() проверяет, что все необходимые данные есть
			if 'NUMBER' not in p:
				raise SystemExit('STOP: The program needs NUMBER')
			if 'X_IMAGE' not in p:
				raise SystemExit('STOP: The program needs X_IMAGE')
			if 'Y_IMAGE' not in p:
				raise SystemExit('STOP: The program needs Y_IMAGE')
			if 'A_IMAGE' not in p:
				raise SystemExit('STOP: The program needs A_IMAGE')
			if 'B_IMAGE' not in p:
				raise SystemExit('STOP: The program needs B_IMAGE')
			if 'ELLIPTICITY' not in p:
				raise SystemExit('STOP: The program needs ELLIPTICITY')
		checkdata(p)
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

		# здесь будет записан номер объекта в словарь
		# а значения для каждого объекта в словаре будут 
		# записываться кортежом
		if float(headline[ellcolumn])>=xell:
			num=int(headline[0])
			data[num]=tuple(float(headline[i]) for i in range(1,np))
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
	if float(line[ellcolumn])>=xell:
		data[int(line[0])]=tuple(float(line[i]) for i in range(1,np))
catalog.close()
if len(data)==0:
	raise SystemExit('STOP: No object in the catalog has e>'+str(xell))

# Нужно создать список X, Y и ELLIPTICITY для regions.
# Функция create_regions должна знать, в каких столбцах находятся 
# вышеупомянутые параметры. Так как в кортеже нумерация с нуля,
# номер колонок из списка p берется со значением на 1 меньшим
xcol=int(p.index('X_IMAGE'))-1
ycol=int(p.index('Y_IMAGE'))-1
elcol=int(p.index('ELLIPTICITY'))-1
regions.create_regions(data,xcol,ycol,elcol,file=image+'r',red=False)

# Если у меня в каталоге есть WIN параметры, то я могу через них высчитать
# параметр эллиптичности и сравнить его со значением ELLIPTICITY.
# Если разница велика, то изофоты такого объекта далеки от эллипсов.
# Я хочу вывести также список red regions, чтобы такие объекты пометить
if 'AWIN_IMAGE' in p and 'BWIN_IMAGE' in p:
	awincol=int(p.index('AWIN_IMAGE'))-1
	bwincol=int(p.index('BWIN_IMAGE'))-1
	data_dell={}
	for i in data.keys():
		lparam=list(data[i])
		lparam[elcol]=1.0-data[i][bwincol]/data[i][awincol]
		delta_e=round(data[i][elcol]-lparam[elcol],3)
		if delta_e>0.3 or delta_e<0.0:
			# В функцию create_regions попадет словарь, у которого
			# вместо эллиптичности указана разность el-elWIN
			lparam[elcol]=delta_e
			data_dell[i]=tuple(lparam)
	fileimage=image+'rred'
	regions.create_regions(data_dell,xcol,ycol,elcol,file=fileimage,red=True)

