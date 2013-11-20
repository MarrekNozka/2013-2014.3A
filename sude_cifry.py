#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  sude_cifry.py
# Datum:   20.11.2013 08:27
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   program načte řádek a vypíše kolik je tam sudých cifer
# Popis:   
############################################################################

radek=raw_input('neco mi sem napis > ')

##############################3
# mala vysvětlující vsuvka
i=0
while i<len(radek):
    print radek[i]
    i = i + 1
##############################
# program 1
pocet=0
i=0
while i<len(radek):
    if radek[i]=='2' or radek[i]=='4' or radek[i]=='6' or radek[i]=='8':
        pocet=pocet+1
    i = i + 1
print "pocet sudych cifer je ", pocet
##############################
# program 2
pocet=0
i=0
while i<len(radek):
    if radek[i]=='2' :
        pocet=pocet+1
    if radek[i]=='4' or radek[i]=='6':
        pocet=pocet+1
    elif radek[i]=='8':
        pocet=pocet+1
    i = i + 1
print "pocet sudych cifer je ", pocet
##############################
# program 3, abych ukázal jak funguje elif
pocet=0
i=0
while i<len(radek):
    if radek[i]=='2' :
        pocet=pocet+1
    elif radek[i]=='4':
        pocet=pocet+1
    elif radek[i]=='6':
        pocet=pocet+1
    elif radek[i]=='8':
        pocet=pocet+1
    else:
        pass
    i = i + 1
print "pocet sudych cifer je ", pocet
