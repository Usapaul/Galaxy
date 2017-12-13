#!/usr/bin/env python
# -*- coding: utf-8 -*-

import regions
import sys

# Получаемые аргументы: имя изображения без расширения
image = sys.argv[1]

# p хранит имена параметров(X, Y, A, B, APER и т.д.)
p = []
# data хранит значения параметров для каждого объекта 
data = {}
catalog = open(image+'best.dat','r')
# Вверху файла у меня заголовочная строка с именами параметров
header = catalog.readline().strip().split()
# np -- Number of Parameters без MY_COMMENT
np = len(header)-1
if header[0] != 'NUMBER':
	raise SystemExit('STOP: NUMBER must be on the 1st line')
if header[-1] != 'MY_COMMENT':
	raise SystemExit('STOP: MY_COMMENT must be on the last position')

# Так как у меня будет словарь data, у которого ключом является 
# NUMBER, а значениями -- кортеж из всего остального, а я хочу
# работать с этими кортежами (у которых нумерация идет с нуля),
# то я заранее скажу, что номер столбцов для x, y и el
# на единицу меньше (первый столбец идет в ключ, а не в кортеж)
xcol = int(header.index('X_IMAGE')) - 1
ycol = int(header.index('Y_IMAGE')) - 1 
elcol = int(header.index('ELLIPTICITY')) - 1

for line in catalog:
	line = line.strip().split()
	floatdata = [float(line[i]) for i in range(1,np)]
	comment = ' '.join(line[np:])
	# Совместим float значения и комментарий в один список
	floatdata.append(comment)
	data[int(line[0])] = tuple(floatdata)
catalog.close()

extrafile = image+'extrar'
regions.create_regions(data,xcol,ycol,elcol,file=extrafile,red=False)
