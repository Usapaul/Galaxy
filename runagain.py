#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import funcs

image = sys.argv[1]

os.system('python3 readcat.py '+image)

commentsfile = open(image+'allcom.dat','r')
# catlg содержит координаты и комментарии только тех объектов, которые 
# не 'ok' и не 'no', потому что ok и no означают, что я уже точно
# решил, что это хороший или плохой объект, и не надо еще раз проверять
catlg = {}
for line in commentsfile:
	line = line.strip().split()
	if ' '.join(line[2:]) in ('ok','no'):
		catlg[(float(line[0]),float(line[1]))]=' '.join(line[2:])
commentsfile.close()

regionsfile = open(image+'r.reg','r')
# savedlines хранит копию файла с regions, только с пропущенными
# строками -- для тех объектов, которые мне не нужны, так как были
# закомментированы как 'ok' или 'no'.
savedlines = []
line = regionsfile.readline().strip()
savedlines.append(line+'\n')
while line != 'image':
	# Предполагается, что файл с regions содержит последней
	# строкой заголовка только слово 'image', и больше 
	# в этой строке ничего не содержится, а после нее
	# идут уже записи с самими "регионами", где через
	# пробел записано все, и X и Y находятся на 
	# второй и третьей позициях в строке !через пробел все!
	line = regionsfile.readline().strip()
	savedlines.append(line+'\n')

for line in regionsfile:
	line = line.strip().split()
	# Напоминаю самому себе, что в строке line сначала
	# записана форма региона (например, circle), а затем
	# через пробелы -- координаты X Y. Поэтому
	# line[0]='circle', line[1&2]= X & Y
	# new_point изменится на False, если при переборе
	# всех точек из catlg
	new_point = True
	for i in catlg.keys():
		print(line[1],line[2],i[0],i[1],True)
		if funcs.check_point(line[1],line[2],i[0],i[1],3):
			new_point = False
			break
	if new_point:
		savedlines.append(' '.join(line)+'\n')
regionsfile.close()
regionsfilenew = open(image+'r.reg','w')
for i in range(len(savedlines)):
	regionsfilenew.write(savedlines[i])
regionsfilenew.close()
