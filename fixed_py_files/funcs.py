#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkdata(p):
# Производится проверка на наличие всех необходимых данных и их корректность
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

# def check_point(x1,y1,x2,y2,d):
# # Проверяется, что точки (x1,y1) и (x2,y2) близкие
# # d задает параметр близости (в пикселях)
# 	x1 = float(x1)
# 	y1 = float(y1)
# 	x2 = float(x2)
# 	y2 = float(y2)
# 	dx = abs(x2-x1)
# 	dy = abs(y2-y1)
# 	return dx+dy < d

def check_point(x1,y1,x2,y2,d):
# Проверяется, что точки (x1,y1) и (x2,y2) близкие
# d задает параметр близости (в пикселях)
	return abs(float(x2)-float(x1)) + abs(float(y2)-float(y1)) < d


border = [0 for i in range(4)]
def whatabound(boundxy):
# Просто выполняется приведение списка из кортежей --
# координат (x,y) углов рамки изображения к такому порядку,
# где грань border[0]-border[1] будет верхней, то есть
# рабочее изображение находится ниже нее. То есть это левый
# верхний и правый верхний углы. А затем пойдут правый
# нижний и левый нижний углы.
# Так как прямоугольник может быть повернут произвольно, то
# уточняю для самого себя, что я хочу описать сначала две 
# границы, для которых изображение будет !ниже! обоих отрезков, 
# соединяющих углы, и затем оставшийся четвертый угол будет, 
# собственно, последним в списке.
# Работает только для прямоугольных изображений!
# -- то есть с некоторыми параллелограммами тоже,
# но нужно смотреть, чтобы границы изображения подходили под
# алгоритм, описанный ниже
	
	global border
	# Просто преобразование всех значений к float:
	for i in range(len(boundxy)):
		border[i]=tuple([float(boundxy[i][j]) for j in 1,2])
	# Хочу, чтобы у меня был словарь, где ключ -- это X,
	# а значение по ключу X_i -- это соответствующее Y_i.
	# Это первое, что в голову пришло просто, как работать с
	# координатами X точно сразу и быстро определять 
	# соответствующую координату Y для точки с конкретным X.
	# И наоборот, хочу иметь такой же быстрый доступ к Xi через Yi
	pointsx = {}
	pointsy = {}
	for i in range(len(border)):
		pointsx[border[i][0]] = border[i][1]
		pointsy[border[i][1]] = border[i][0]
	x4 = [border[i][0] for i in range(4)]
	y4 = [border[i][1] for i in range(4)]
	border[0] = tuple(min(x4),pointsx[min(x4)]) 
	border[1] = tuple(pointsy[max(y4)],max(y4))
	border[2] = tuple(max(x4),pointsx[max(x4)])
	border[3] = tuple(pointsy[min(y4)],min(y4))
	return border

bound_a0 = 0.0
bound_b0 = 0.0
bound_a1 = 0.0
bound_b1 = 0.0
bound_a2 = 0.0
bound_b2 = 0.0
bound_a3 = 0.0
bound_b3 = 0.0

def compute_a_b_for_bound():
# Выполняется создание глобальных переменных a и b, значения которых
# соответствуют наклюну четырех прямых, составляющих границу	
	dx = [0 for i in range(4)]
	dy = [0 for i in range(4)]
	for i in range(3):
		dx[i] = border[i+1][0] - border[i][0]
		dy[i] = border[i+1][1] - border[i][1]
	dx[3] = border[0][0] - border[3][0]
	dy[3] = border[0][1] - border[3][1]

	global bound_a0
	global bound_b0
	global bound_a1
	global bound_b1
	global bound_a2
	global bound_b2
	global bound_a3
	global bound_b3

	bound_a0 = dy[0] / dx[0]
	bound_b0 = border[0][1] - bound_a0 * border[0][0]
	bound_a1 = dy[1] / dx[1]
	bound_b1 = border[1][1] - bound_a1 * border[1][0]
	bound_a2 = dy[2] / dx[2]
	bound_b2 = border[2][1] - bound_a2 * border[2][0]
	bound_a3 = dy[3] / dx[3]
	bound_b3 = border[3][1] - bound_a3 * border[3][0]

def check_bound(x,y):
# Проверка, попадает ли (x,y) в прямоугольник,
# ограниченный рамкой, координаты углов которой
# записаны в списке border, каждый его элемент --
# кортеж из координат углов (x,y)
	x = float(x)
	y = float(y)
	inside = True
	if y > bound_a0 * x + bound_b0:
		inside = False
	if y > bound_a1 * x + bound_b1:
		inside = False
	if y < bound_a2 * x + bound_b2:
		inside = False
	if y < bound_a3 * x + bound_b3:
		inside = False