#!/usr/bin/env python
# -*- coding: utf-8 -*-


# X=int(input())
# H=int(input())
# M=int(input())
# X+=H*60+M
# h=X//60
# m=X%60
# print(h)
# print(m)


#x = 5
#y = 10
#print(y > x * x or y >= 2 * x and x < y)

#T and F or not T and not F
#   F 		 F		   T
#   F			  F
#   		F


#A=int(input())
#B=int(input())
#H=int(input())
#
#if H<A:
#	print('Недосып')
#elif H<=B:
#	print('Это нормально')
#else:
#	print('Пересып')




#y=int(input())
#if y%4==0:
#	if y%100!=0:
#		print('Високосный')
#	elif y%400!=0:
#		print('Обычный')
#	else:
#		print('Високосный')
#else:
#	print('Обычный')


#a=int(input())
#b=int(input())
#c=int(input())
#p=(a+b+c)/2
#print((p*(p-a)*(p-b)*(p-c))**0.5)

#a=int(input())
#print(not(a<=-15 or 12<a<=14 or 17<=a<19))

#a=float(input())
#b=float(input())
#o=input()
#
#if o=='+':
#	print(a+b)
#if o=='-':
#	print(a-b)
#if o=='/':
#	if b!=0:
#		print(a/b)
#	else:
#		print('Деление на 0!')
#if o=='*':
#	print(a*b)
#if o=='mod':
#	if a>0 and b>0:
#		print(a/b-int(a/b))
#	elif a<0 and b>0:
#		print((a/b-int(a/b)+1)*b)
#	else:
#		print('Деление на 0!')
#if o=='pow':
#	if a!=0:
#		print(a**b)
#	elif b>0:
#		print(a**b)
#	else:
#		print('Деление на 0!')
#if o=='div':
#	if b!=0:
#		print(int(a/b))
#	else:
#		print('Деление на 0!')#






#typeform=input()
#
#if typeform=='треугольник':
#	a=float(input())
#	b=float(input())
#	c=float(input())
#	p=((a+b+c)/2)
#	s = (((p*(p-a)*(p-b)*(p-c)))**0.5)
#	print(s)
#if typeform=='прямоугольник':
#	a=float(input())
#	b=float(input())
#	print(a*b)
#if typeform=='круг':
#	r=float(input())
#	print(3.14*r**2)



# a=int(input())
# b=int(input())
# c=int(input())
# minx=a
# maxx=a
# mid=a
# 
# if b<a:
# 	minx=b
# 	if c<b:
# 		minx=c
# 		mid=b
# if c<a:
# 	minx=c
# 
# if a<b:
# 	maxx=b
# 	if b<c:
# 		maxx=c
# if a<c:
# 	maxx=c
# 
# print(maxx)
# print(minx)
# if maxx!=a and minx!=a

# a=int(input())
# b=int(input())
# c=int(input())
# 
# abc=[a,b,c]
# minx=min(abc)
# abc=abc.remove(minx)
# maxx=max(abc)
# abc=abc.remove(maxx)
# midx=sum(abc)
# 
# print(minx)
# print(maxx)
# print(midx)



# n=int(input())
# 
# if n%100<10 or n%100>15:
# 	if n%10==0:
# 		print(n,'программистов')
# 	elif n%10==1:
# 		print(n,'программист')
# 	elif 2<=n%10<=4:
# 		print(n,'программиста')
# 	else:
# 		print(n,'программистов')
# else:
# 	print(n,'программистов')

# number=input()
# 
# left=int(number[0])+int(number[1])+int(number[2])
# right=int(number[3])+int(number[4])+int(number[5])
# 
# print(type(left),type(right))
# 
# if left==right:
# 	print('Счастливый')
# else:
# 	print('Обычный')


#a=int(input())
#b=int(input())
#
#
#i=1
#
#while i%a!=0 or i%b!=0 :
#	i=i+1
#print(i)



# a=int(input())
# b=int(input())
# s=0
# for i in range(a,b+1):
# 	if i%3==0:
# 		s+=i
# 
# s/=len(range(a,b+1))
# print(s)

# s=[1,2,3]
# s+='xx'
# print(s)
# 




# a=[int(i) for i in input().split()]
# a.sort()
# b=[]
# i=1
# j=1
# while j<len(a):
#     if a[j]==a[j-1]:
#         b.append(a[j])
#         j+=1
#     else:
#         if len(b)>1:
#             print(b[0],end=' ')
#         b=[]
#         j+=1

# a=[]
# a.append(int(input()))
# while sum(a)!=0:
# 	a.append(int(input()))
# print(sum([i**2 for i in a]))

#n=int(input())
#a=[]
#for j in range(n):
#	for i in range(j+1):
#		a.append(j+1)
#for j in range(n):
#	print(a[j],end=' ')



# lst=[int(i) for i in input().split()]
# x=int(input())
# print(lst)
# print(x)
# ind=[]
# if lst.count(x)>0:
# 	print(lst.count(x))
# 	j=0
# 	for i in range(lst.count(x)):
# 		ind.append(lst.index(x)+j)
# 		print(lst.index(x))
# 		print(i)
# 		lst.remove(x)
# 		j+=1
# 		print(lst)
# 		print('lol',ind[i],'lol')
# else:
# 	print('Отсутствует')



# a=[]
# box=input()
# while box!='end':
# 	a.append([int(i) for i in box.split()])
# 	box=input()
# b=[[0 for i in range(len(a[0]))] for i in range(len(a))]
# for i in range(len(a)):
# 	for j in range(len(a[0])):
# 		b[i][j]=a[i-1][j]+a[(i+1)%len(a)][j]+a[i][j-1]+a[i][(j+1)%len(a[0])]
# 
# for i in range(len(b)):
# 	for j in range(len(b[i])):
# 		print(b[i][j],end=' ')
# 	print()


# n=int(input())
# matr=[[0 for i in range(n)] for j in range(n)]
# # grad обозначает число в градусах, по какому направлению движемся,
# # а "нулевое" направление -- вправо, и далее по часовой стрелке
# grad=0
# # k -- номер текущего записываемого элемента спирали
# # стартовое значение равно 1
# k=1
# # i и j являются индексами "ячейки" матрицы,
# # на которой остановились на предыдущем шаге (по отношению 
# # к текущему k), переходя из ячейки в ячейку, заполняя спираль
# # стартовые значения равны 0 и -1, потому что начинаем движение
# # от ячейки [0][0] вправо, словно "входим" в матрицу с ячейки [0][-1]
# i=0
# j=-1
# while k<=n**2:
# 	# direction: 0 = right, 1 = down, 2 = left, 3 = up
# 	direction=(grad//90)%4
# 	if i!=0 or j!=0:
# 		print(k,direction,'i and j:',i,j)
# 	if direction==0:
# 		# "пока" не упремся в заполненную ячейку или в край матрицы
# 		while 0<=j+1<n and matr[i][j+1]==0:
# 			j+=1
# 			matr[i][j]=k
# 			k+=1
# 		grad+=90
# 	if direction==1:
# 		while 0<=i+1<n and matr[i+1][j]==0:
# 			i+=1
# 			matr[i][j]=k
# 			k+=1
# 		grad+=90
# 	if direction==2:
# 		while 0<=j-1<n and matr[i][j-1]==0:
# 			j-=1
# 			matr[i][j]=k
# 			k+=1
# 		grad+=90
# 	if direction==3:
# 		while 0<=i-1<n and matr[i-1][j]==0:
# 			i-=1
# 			matr[i][j]=k
# 			k+=1
# 		grad+=90
# 
# for i in range(n):
# 	for j in range(n):
# 		print(matr[i][j],end=' ')
# 	print()
# 
# 


# n=int(input())
# matr=[[0]*n for i in range(n)]
# 
# for i in range(n//2+1):
#	lu=i
#	ru=n-i
#
#	print([sum([4*(n-1-2*k) for k in range(i)])+j for j in range(1,n-i+1)])
#
#	print(i+1,n-i-1,n-1-i)
#	print(matr[n-i-1][n-1-i])
#	print('ok-1')
#	print(matr[1:2])
#	print(matr[1][2])
#	print(matr[1:2][2])
#	print('ok0')
#	print([matr[i][n-1-i]+j for j in range(1,n-i+1)])
#	print(len(matr[i][i:n-i]),len([sum([4*(n-1-2*k) for k in range(i)])+j for j in range(1,n-i+1)]))

#	matr[i][i:n-i]=[sum([4*(n-1-2*k) for k in range(i)])+j for j in range(1,n-i+1)]
#	print('ok1')
#	
#	matr[i+1:n-i][n-1-i]=[matr[i][n-1-i]+j for j in range(1,n-i+1)]
#	print('ok2')
#	matr[n-1-i][i:n-i-1]=[matr[n-1-i][n-1-i]+j for j in range(n-i,0,-1)]
#	print('ok3')
#	matr[i+1:n-1-i][i]=[matr[n-1-i][i]+j for j in range(n-i,0,-1)]
#	print('ok4')


#	matr[i][i:n-1-i]=[sum([4*(n-1-2*k) for k in range(i)])+j for j in range(1,n-i+1)]
#	matr[i+1:n-1-i][n-1-i]=[matr[i][n-1-i]+j for j in range(1,n-i+1)]
#	matr[n-1-i][i:n-1-i]=reversed([matr[n-1-i][n-1-i]+j for j in range(1,n-i+1)])
#	matr[i+1:n-2-i][i]=reversed(matr[n-1-i][i]+j for j in range(1,n-i+1))
#	lenta=[sum([4*(n-1-2*k) for k in range(i)])+j for j in range(1,4*(n-i)-3)]
#	matr[i][i:n-1-i]=lenta[:n-1-2*i]
#	matr[n-1-i][i+1:n-1-i]=lenta[n-2*i:n-2*i]	
#for i in range(n):
#	for j in range(n):
#		print(matr[i][j],end=' ')
#	print()


# 
# def fun(x):
# 	if x<=-2:
# 		return 1-(x+2)**2
# 	if -2<x<=2:
# 		return -x/2
# 	if x>2:
# 		return (x-2)**2+1
# 
# 

# l=[1,2,3,4,5,6]
# l=[10,5,8,3]
# l=[1,2]
# l.clear()
# print([i//2 for i in l if i%2==0])
# l=[i//2 for i in l if i%2!=1]
# print([i//2 for i in l if i%2==0])

# a=[i for i in input().split()]
# d={}
# for i in range(len(a)):
# 	print(a[i])
# 	x=a[i]
# 	x=x.lower()
# 	a[i]=x
# 	print(a[i])
# 	d[a[i]]=0
# print(d)
# for i in a:
#     d[i]+=1
# for i in d.keys():
#     print(i,d[i])





# infile=open('fdata.dat','r')
# string=infile.readline()
# s=string.strip()
# infile.close()
# 
# d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# 
# s0=''
# i=0
# while i<len(s):
# 	if s[i] in d:
# 		j=i
# 		count=int(s[j])
# 		while j+1<len(s) and s[j+1] in d:
# 			j+=1
# 			count=int(str(count)+s[j])
# 		s0+=s[i-1]*count
# 		i=j
# 	i+=1
# 
# outfile=open('ddata.dat','w')
# outfile.write(s0)
# 
# 
# 


# s=[]
# 
# infile=open('fdata.dat','r')
# for line in infile:
# 	s.extend(line.split())
# infile.close()
# d={}
# for i in range(len(s)):
# 	s[i]=s[i].lower()
# 	d[s[i]]=0
# 
# sall=[]
# for i in range(len(s)):
# 	sall+=s[i]
# 	d[s[i]]+=1
# 
# st=[]
# dv=[]
# dv+=d.values()
# maxx=max(dv)
# for i in d.keys():
# 	if d[i]==maxx:
# 		st.append(i)
# 
# st.sort()
# 
# outfile=open('ddata.dat','w')
# outfile.write(st[0]+' '+str(maxx))
# outfile.close()
# 
# 
# 
# 

# d={}
# linel=[]
# infile=open('fdata.dat','r')
# outfile=open('ddata.dat','w')
# for line in infile:
# 	linel=line.strip().split(';')
# 	d[linel[0]]=linel[1:4]
# 	x=int(linel[1])
# 	y=int(linel[2])
# 	z=int(linel[3])
# 	outfile.write(str((x+y+z)/3)+'\n')
# infile.close()
# sall=[]
# xall=[]
# yall=[]
# zall=[]
# for i in d.keys():
# 	xall.append(int(d[i][0]))
# 	yall.append(int(d[i][1]))
# 	zall.append(int(d[i][2]))
# outfile.write(str(sum(xall)/len(d))+' '+str(sum(yall)/len(d))+' '+str(sum(zall)/len(d)))
# outfile.close()
# 
# 
# 
# 
# 


# import requests
# 
# 
# 
# r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
# 
# rfile=r.text
# names=''
# for line in rfile.splitlines():
# 	names=line
# 	count=1
# 	print(names)
# 
# while True:
# 	r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+names)
# 	rfile=r.text
# 	names=''
# 	count=2
# 	for line in rfile.splitlines():
# 		names=line
# 		if count<15:
# 			print(names)
# 			print(r.text)
# 			print('======================================')
# 			print('======================================')
# 			print('======================================')
# 	if names[0:2]=='We':
# 		print(r.text)
# 		print('=========================================')
# 		break
# 
# #while line in rfile:
# #	count+=1
# 
# print(count)

