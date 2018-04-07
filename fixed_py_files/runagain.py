#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import funcs

image = sys.argv[1]
# Если sys.argv[2] == 1, то надо исключать объекты, которые находятся
# в рамке-полосе на границе изображения, и по существу состоят
# лишь из шума
boundxy = [0 for i in range(4)]
# boundfire -- индикатор, который говорит о том, что нужно 
# отбрасывать граничные объекты
boundfire = False
if len(sys.argv) > 2:
	if sys.argv[2] == 1:
		boundfire = True
		boundxy[0] = (583,1259)
		boundxy[1] = (1124,8133)
		boundxy[2] = (7997,7029)
		boundxy[3] = (7640,290)
		boundxy = funcs.whatabound(boundxy)
		funcs.compute_a_b_for_bound()

os.system('python3 readcat.py '+image)

commentsfile = open(image+'allcom.dat','r')
# catlg содержит координаты и комментарии только тех объектов, которые 
# 'ok' или 'no', потому что ok и no означают, что я уже точно
# решил, что это хороший или плохой объект, и не надо еще раз проверять
# и ниже я хочу проверять каждый новый объект на предмет наличия в 
# словаре catlg с комментарием 'ok' или 'no', и исследовать его не буду
catlg = {}
for line in commentsfile:
	line = line.strip().split()
	if ' '.join(line[2:]) in ('ok','no'):
		catlg[(float(line[0]),float(line[1]))] = ' '.join(line[2:])
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
		# Если нужно исключать объекты на границе, то 
		# boundfire должно иметь значение True, присвоенное
		# переменной еще в начале программы на стадии обработки
		# аргументов командной строки. А тогда check_bound
		# будет, собственно, проверять, попадает ли объект в 
		# "разрешенные" границы изображения, или нет.
		if boundfire == True:
			if not funcs.check_bound(line[1],line[2]):
				break
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
