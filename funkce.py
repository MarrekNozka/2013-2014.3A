#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  funkce.py
# Datum:   26.02.2014 08:50
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL 
############################################################################


def jmeno(a,b,c):
    a=a*100
    b*=10
    c=c
    return a+b+c


a=7777777777777777777
b=8888888888888888888
bagr=8

"""
Proměnné a,b,c jsou uzavřeny ve funkci jmeno.
Nemůžou ven, a proto neovlivňují proměnné a,b,c hlavního programu.
"""

print a,b
print '--------------------------'
print jmeno(bagr,bagr,1)
vysledek = jmeno(2,4,9) + jmeno(4,5,1)
print vysledek

print jmeno(2,7,8)

print '--------------------------'
print a,b
#print c
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%'

def nijak(a):
    """do bagr nepřiřazuji jen čtu"""
    return a+bagr

"""
Proměnná barg existuje v hlavním jmenném prostroru 
a lze ji použít uvnitř funkce
"""
bagr=44

print nijak(20)

print '%%%%%%%%%%%%%%%%%%%%%%%%%%%'

def spatne(a):
#    global bagr
#    print bagr
    bagr=a*a
    """do bagr přiřazuji, proto je to LOKÁLNÍ proměnná"""
    return bagr

bagr=44
print spatne(16)
print bagr
