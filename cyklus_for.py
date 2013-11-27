#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cyklus_for.py
# Datum:   27.11.2013 08:36
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Cyklus for
############################################################################



print "##########################"
for i in (1,2,10,30, 54) :
    print i, i*i, i**3, i**4
print "##########################"

seznam = [ 'ahoj', 'nazdar', 'cau' ]
for slovo in seznam :
    print slovo
    print slovo.upper()
print "##########################"

for a in range(1,11):
    for b in range(1,11):
        print '{0:5d}x{1:4d}={2:2d}'.format(a,b,a*b)

for pismenko in "ahoj Karle":
    print pismenko,  # čárka na konci znamená, že se nezalomí řádek
    print ' ', 
print

x,y = 'cislox', 'cisloy'

seznam=[ [1,2], [33,44], [888,777]  ] 
for a,b in seznam:
    print a,b
    print ( a*a + b*b )**0.5

s='ahoj Karle'
for i,znak in enumerate(s):
    print i,':',znak
