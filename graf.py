#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  graf.py
# Datum:   12.03.2014 08:34
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Program čte textový soubor a vykresluje graf
############################################################################

jmenosouboru='graf.txt'
hodnotyX=[]
hodnotyY=[]
# Načtení souboru
f = open(jmenosouboru, 'r')
while True:
    radek = f.readline()
    if radek=='':
        break   # když dojdu na konec souboru vyskočím z cyklu
    radek = radek.strip() # odstraní bílé znaky na začátku a konci
    # zpracování řádku
    if radek=='' or '-----' in radek or radek[0]=='#':
        continue    # horizontální čáru nezpracovávám
    x,y = radek.split() 
    hodnotyX.append(x)
    hodnotyY.append(y)
# vyndám popisky
popisekX= hodnotyX.pop(0)
popisekY= hodnotyY.pop(0)

nahradCarky(hodnotyX)
nahradCarky(hodnotyY)

import pylab

pylab.plot(hodnotyX,hodnotyY)
pylab.show()

