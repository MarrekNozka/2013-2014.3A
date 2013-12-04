#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  ctverce.py
# Datum:   04.12.2013 08:37
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Popis:   program generuje náhoná čísla
#          potom počítá součet jejich čtverců
############################################################################

import random

#print random.randint(-10,10)
cisla=[]
for i in range(4):
    cisla=cisla+[random.randint(0,5)]

print cisla

soucet=0
for x in cisla:
    mocnina = x*x
    soucet = soucet + mocnina

print "sucet je ", soucet
