#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  myfnc.py
# Datum:   09.04.2014 08:55
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   malý modul pro moje vlastní funkce
############################################################################
from __future__ import unicode_literals


def exp(x):
    """ exp(x) -> vrátí hodnotu exponenciální funkce
                  e na x
    """
    vysl = 1
    citatel = float(x)
    jmenovatel = 1.
    n = 1
    while citatel/jmenovatel > 1e-6:
        vysl += citatel/jmenovatel
        citatel *= x
        n += 1
        jmenovatel *= n
    return vysl


def mocnina(x, y):
    return x**y
