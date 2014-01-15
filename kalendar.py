#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  kalendar.py
# Datum:   15.01.2014 08:33
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
############################################################################


print 10,
print 20,
print 30,
print

radek=''
radek = radek+str(17)+' '
radek += str(27)+' '
radek += str(37)
radek += ' '
radek += '\n'
radek += ' ahoj'
radek += ' nazdar'
radek += "cislo:{0:8d}:".format(31)

print radek
print '------------------------------'

print "Po Ut St Čt Pá So Ne"
prvni=3  # první den v měsíci je čtvrtek (pondělí je 0)
i = 1
radek = prvni*3 * ' '
while i<=31:
    radek = radek + "{0:2d}".format(i) + ' '
    if i%(7) == 7-prvni :
        radek += '\n'
    i = i+1
print radek
