#!/usr/bin/env python
# -*- coding: utf8 -*-

a=input('zadej cislo: ')  # funkce input vrací číslo tj. int, float
aa=a
#a=raw_input('zadej retezec') # funkce vrací řetězec
#a=int(a)


if a==0:
    print 'A je NULA'
    b='ANO'
else:
    print 'A je nenulové'
    b='NE'
print 'Tohle se napiše vždy'


while a > 0 :
    a=a-1
    print a
print 'A tohle je konec!!!'

print '###################################'

while aa>0:
    aa=aa-1
    if aa%2 == 0 : # a je sude
        print aa
print 'A tohle FAKT je konec!!!'