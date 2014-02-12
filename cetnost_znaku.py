#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cetnost_znaku.py
# Datum:   12.02.2014 08:50
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   četnost jednotlivých znaků v textu
###########################################################################

# vytvořžím slovník, počet pro každé písmeno abecedy je 0
cetnost = {}
znaky=sorted(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

for pismeno in znaky:
    cetnost[pismeno] = 0

# načtu text
text=raw_input('Zadej text > ')

# počítám znaky
for pismeno in text:
    pismeno = pismeno.upper()
#   if ord(pismeno)>=ord("A") and ord(pismeno) <= ord('Z'):
    if pismeno in znaky:
        cetnost[pismeno] +=1

# vypíšu na obrazovku
for pismeno in znaky:
    if cetnost[pismeno]>0 :
        print pismeno,'->', cetnost[pismeno]

# vypíšu na obrazovku podruhé
for pismeno, pocet in cetnost.items():
    if pocet>0 :
        print pismeno,'->', pocet

