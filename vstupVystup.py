#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vstupVystup.py
# Datum:   06.11.2013 09:06
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   demonstrace vstupu a výstupu
############################################################################

a = input('zadej cislo: ')
print(a)
print(type(a))

b = raw_input('zadej znak: ')
print(b)
print(type(b))

radek = raw_input('neco misem napis: ')
seznam=radek.split()
print(seznam)
print(type(seznam))

i=0
while i<len(radek):
    print(radek[i])
    i=i+1

i=0
while i<len(seznam):
    print(seznam[i])
    i=i+1

cisla=raw_input('zadem mi cisla, ja udelam prumer :')
cisla=cisla.split()
print cisla

i=0
suma=0.0
while i<len(cisla):
    suma = suma+float(cisla[i])
    i=i+1
print(suma/len(cisla))
