# Для работы с Sextractor:
# Создание каталога extracted objects;

# readcat.py считывает весь каталог и сохраняет
# в файлах с расширением .reg список объектов с 
# ellipticity>0.7, соответственно, сохраняет в 
# таком формате, который можно сразу загрузить
# в ds9 как список regions;

# Скрипт panning.py запускает ds9 и выполняет 
# перемещение по изображению с помощью команды pan.
# Для скрипта нужно, чтобы вместе с его запуском
# были переданы аргументы: {nameimage}, {indicator},
# [>=1 файла с координатами .reg или другого формата]:
# если будет подан файл .reg, то оттуда правильным образом
# будут взяты координаты. А если другое расширение, то
# предполагается, что в каждой строке записано X Y [smth.else]
# indicator=0, если хочется только посмотреть на объекты, и
# =1, если нужно записывать комментарии с экрана

# {nameimage }без указания расширения .fits. При этом в папке \
# должен также содержаться файл {nameimage}aper.fits;

# saving.py сохраняет данные из исходного каталога 
# в таком же его виде, только последний столбец --
# комментарий, записанный для каждого объекта во время 
# выполнения скрипта.

#==========================================================

# Переменную image нужно менять явно из командной строки
image=Noimage
# default.* -- конфигурационные файлы для sextractor
conf=default
alldefault=$(conf).sex $(conf).param $(conf).nnw $(conf).conv $(conf).psf

createcat : saving.py $(image)comments.dat $(image)field.cat
	python3 saving.py $(image)

# Файлы .reg можно заменить любыми другими
$(image)comments.dat : panning.py $(image)r.reg $(image).fits $(image)aper.fits
	python3 panning.py $(image) 1 $(image)r.reg

$(image)r.reg : readcat.py $(image)field.cat
	python3 readcat.py $(image)

$(image)field.cat $(image)aper.fits : $(image).fits $(alldefault)
	sex $(image).fits \
	-CHECKIMAGE_TYPE APERTURES \
	-CHECKIMAGE_NAME $(image)aper.fits \
	-CATALOG_NAME $(image)field.cat

look : 
	python3 panning.py $(image) 0 $(image)comments.dat

check : $(image)best.dat
	python3 checkagain.py $(image)
	python3 panning.py $(image) 1 $(image)extrar.reg

newstart : 
	python3 runagain.py $(image)
	python3 panning.py $(image) 1 $(image)r.reg
