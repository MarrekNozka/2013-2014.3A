#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  soucty.py
# Datum:   04.12.2013 08:37
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Popis:   program  sečte zvláš všechna kladná čísla
#          a zvlášť všechna záporná čísla
############################################################################

import random

cisla=[]
for i in range(6):
    cisla=cisla+[random.randint(-5,5)]

print cisla

kladna=0
zaporna=0
for x in cisla:
    if x<0 :
        zaporna += x # stejné jako  zaporna = zaporna + x
    else:
        kladna = kladna + x

print kladna, zaporna
