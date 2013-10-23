# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/marek/.spyder2/.temp.py
"""

import pylab
import math, copy

#x = [1, 2, 3]
#y = [5, 2, 8]
#pylab.plot(x,y,'o-')  

x=[0.0]
y=[math.sin( x[-1] )]  # x[-1] je poslední hodnota v seznamu
while x[-1] <= 4  :
    x = x + [ x[-1]+0.8]  #  přidám do seznamu číslo o 0.1 větší než je poslední hodnota
    y = y + [ math.sin( x[-1] ) ]  # do seznamu y přidám funkční hodnotu pro poslení x

pylab.plot(x,y)

# Vytvořím druhý seznam a budu ho midifikovat tak abych dostal
# absolutní hodnotu 
absy = copy.deepcopy(y)

i = 0 
while i<len(y):
    absy[i] = abs( absy[i] )
    i=i+1

pylab.plot(x,absy)



pylab.show()  