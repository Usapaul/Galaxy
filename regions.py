#!/usr/bin/env python
# -*- coding: utf-8 -*-


def create_regions(catlg,xcol,ycol,elcol,file='regions',red=False):
# Из словаря catlg берутся значения NUMBER (ключ), X, Y и ELLIPTICITY
# и затем создается файл с именем $(file).reg 
# [*]col -- номера колонок с соответствующими параметрами.
# Если нужны "red regions" (где эллиптичность через AWIN и BWIN сильно 
# отличается от значения ELLIPTICITY), то нужно присвоить True
	rcircle=25
	color='blue'
	# regions в подписи для объекта есть запись e=0.[]
	# для red regions нужно de=0.[]. maybe_d == 'd' для red regions
	maybe_d=''
	if red==True:
		rcircle=11
		color='red'
		maybe_d='d'
		file='red'+file

	f=open(file+'.reg','w')
	f.write('# Region file format: DS9 version 4.1\n')
	f.write('global color=green dashlist=8 3 width=1 ')
	f.write('font="helvetica 6 normal roman" ')
	f.write('select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 ')
	f.write('delete=1 include=1 source=1\n')
	f.write('image\n')

	# Проверка, есть ли комментарии для объекта
	# Если есть, то комментарий будет записан в конце кортежа в словаре
	onekey=list(catlg.keys())[0]
	if isinstance(catlg[onekey][-1],str):
		comments_given=True
	else:
		comments_given=False
		comment=''
	for i in catlg.keys():
		x=catlg[i][xcol]
		y=catlg[i][ycol]
		el=catlg[i][elcol]
		if comments_given:
			comment=' '+catlg[i][-1]
		line='circle '+str(x)+' '+str(y)+' '+str(rcircle)+' '
		line+='# '+'color = '+color+' text = { '
		line+=str(i)+' '+maybe_d+'e='+str(el)+comment+' }\n'
		f.write(line)

	f.close()
