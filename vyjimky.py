#!/usr/bin/python
# -*- coding: utf8 -*-
from __future__ import unicode_literals

x = raw_input('zadej  cislo > ')

try:
    print 5*7
    print 5*12
    print 5*int(x)
    print 'dfd'*'fjdkfjdk'
except ValueError:
    print('musíš zadat opravdu číslo')
except KeyboardInterrupt:
    print('uživtel ukončil program')
except:
    print('jiná chyba')
