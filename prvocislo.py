#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prvocislo.py
# Datum:   04.12.2013 09:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   zjisti jestli je zadané číslo prvočíslo
############################################################################

cislo = input('zadej cislo > ')

for i in range(2,cislo):
    if cislo % i == 0 : # cislo je delitelne i
        print "NEEEEE"
        print "je delitelne", i
        exit()
print "Ano ANO Hurá"
