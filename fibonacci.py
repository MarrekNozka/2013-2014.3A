#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   05.03.2014 08:59
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Fibonacciho posloupnost
############################################################################


"""
Rekurzivní výpočet Fibonacciho posloupnoti
"""
def fibonacci(n):
    if n==0 or n==1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def faktorial(n):
    if n<1:
        return 0
    if n==1:
        return 1
    else:
        return n * faktorial(n-1)

for i in range(36):
    print i,' -> ', faktorial(i)

print '-----------------------------'

for i in range(36):
    print i," -> ", fibonacci(i)

