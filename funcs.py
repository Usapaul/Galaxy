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

def check_point(x1,y1,x2,y2,d):
# Проверяется, что точки (x1,y1) и (x2,y2) близкие
# d задает параметр близости (в пикселях)
	x1 = float(x1)
	y1 = float(y1)
	x2 = float(x2)
	y2 = float(y2)
	dx = abs(x2-x1)
	dy = abs(y2-y1)
	return dx+dy < d

def whatabound(border):
# Просто выполняется приведение списка из кортежей --
# координат (x,y) углов рамки изображения к такому порядку,
# где грань border[0]-border[1] будет верхней, то есть
# рабочее изображение находится ниже нее. То есть это левый
# верхний и правый верхние углы. А затем пойдут правый
# нижний и левый нижний углы
	x4=[border[i][0] for i in range(4)]
	y4=[border[i][1] for i in range(4)]
	

def check_bound(x,y,border):
# Проверка, попадает ли (x,y) в прямоугольник,
# ограниченный рамкой, координаты углов которой
# записаны в списке border, каждый его элемент --
# кортеж из координат углов (x,y)
	x = float(x)
	y = float(y)
