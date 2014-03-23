#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  graf.py
# Datum:   12.03.2014 08:34
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Program čte textový soubor a vykresluje graf
############################################################################

def prevedNaCisla(seznamRetezcu):
    """ Funkce vezme seznam řetězců,
          - nahradí v nich desetiné čárky desesetinými tečkami
          - převede řetězce na float

        Vrátí seznam čísel
    """
    vysledek=[]
    for s in seznamRetezcu: 
        vysledek.append( float( s.replace(',','.') ) )
    return vysledek


jmenosouboru='graf.txt'
import os.path
if not os.path.isfile(jmenosouboru):
    jmenosouboru=raw_input("Zadej jméno souboru > ")


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
    x,y = radek.split('|') 
    hodnotyX.append(x)
    hodnotyY.append(y)
f.close()

# vyndám popisky
popisekX= hodnotyX.pop(0)
popisekY= hodnotyY.pop(0)

x = prevedNaCisla(hodnotyX)
y = prevedNaCisla(hodnotyY)


import pylab as lab
import scipy.interpolate as interpol

# vytvořím si novou osu X, ktetá bude mí 300 bodů
xx=lab.linspace(min(x),max(x),300)
# funkce pro výpočet nových hodnoty Y
funkceProlozeni=interpol.UnivariateSpline(x,y,s=1,k=2)
# výpočet nových hodnot Y
yy = funkceProlozeni(xx)

lab.plot(x,y,'r+')
lab.plot(xx,yy,'-g')
lab.grid(True)
lab.xlabel(popisekX.decode('UTF8'))
lab.ylabel(popisekY.decode('UTF8'))


lab.show()
