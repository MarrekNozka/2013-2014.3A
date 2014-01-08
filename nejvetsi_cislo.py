#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  nejvetsi_cislo.py
# Datum:   08.01.2014 09:07
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Program hledá největší/nejmenší číslo v seznamu
############################################################################

import random

seznam = [ random.randint(1,99) for i in range(20) ]
# předchozí a následující řádky dělají to stejné
seznam=[]
for i in range(20):
    seznam = seznam + [ random.randint(1,99) ]
##########################################################

print seznam

nej = seznam[0]
i = 1
while i < len(seznam):
    if seznam[i] > nej:
        nej = seznam[i]
    i += 1
print nej

########################################################

nej = seznam[0]
for cislo in seznam :
    if cislo > nej:
        nej = cislo
print nej


