#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prvocisla.py
# Datum:   05.03.2014 08:31
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   program vypíše prvočísla menší než 1000
############################################################################

def prvocislo(cislo):
    """
    Funkce vrátí True  nebo False pokud cislo je 
    nebo není prvočíslo.
    """
    if cislo <=1 :
        return False
    for i in range(2,cislo/2):
        if cislo%i==0:
            return False
    return True


for i in range(1000):
    if prvocislo(i) :
        print i,
print 
