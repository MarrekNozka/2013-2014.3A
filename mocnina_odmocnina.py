#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  mocnina_odmocnina.py
# Datum:   20.11.2013 08:56
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Je dána posloupnost celých čísel oddělených mezerou.
#          Pro záporná čísla vypište na obrazovku jejich druhou mocninu.
#          Pro kladná čísla vypište na obrazovku jejich odmocninu.
############################################################################

radek = raw_input('zadej cela cisla oddelena mezerou > ')

# prevedu string na list
# promena cisla je list, který obsahuje stringy
cisla = radek.split()

i=0
while i<len(cisla):
    cislo = int( cisla[i] ) # převedu řetězec na číslo ( str na int )
    if cislo <=0:
        print cislo**2
    else:
        print cislo**0.5
    i = i+1
