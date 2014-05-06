#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kalkulacka.py
# Datum:   30.04.2014 08:42
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   jednoduchá reverzní kalkulačka
############################################################################

from __future__ import unicode_literals

zasobnik = []


def zpracujVstup():
    global zasobnik
    vstup = raw_input('>> ').strip()
    if vstup == '':
        print zasobnik
        return
    elif vstup in '+-*/':
        if len(zasobnik) >= 2:
            b = zasobnik.pop()
            a = zasobnik.pop()
        else:
            print ">>>> V zásobníku je málo čísel"
            print zasobnik
            return
        if vstup == '+':
            zasobnik += [a+b]
        elif vstup == '-':
            zasobnik += [a-b]
        elif vstup == '*':
            zasobnik += [a*b]
        elif vstup == '/':c
            zasobnik += [a/b]
        return
    try:
        vstup = float(vstup)
        zasobnik += [vstup]
    except ValueError:
        print ">>>> Zadej jedno reálné číslo"


while True:
    try:
        zpracujVstup()
    except EOFError:
        exit(0)
    except KeyboardInterrupt:
        print "Aplikace ukončena uživatelem"
        exit(1)
#    except:
#        print "ERROR: neznámá chyba"
#        exit(2)
