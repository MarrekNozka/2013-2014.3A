#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  bombardier.py
# Datum:   7.5.2014
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   malá zábavná hra.
###################################################

import random
import pylab as lab
import matplotlib.animation as animation

############################################
SIRKA = 4    # 64
VYSKA = 3    # 23
############################################


def on_key(event):
    print('you pressed', event.key, event.xdata, event.ydata)


def step(event):
    pass


############################################

data = [[1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]


############################################
fig = lab.figure()
sub = lab.subplot(111)
sub.axes.get_xaxis().set_visible(False)
sub.axes.get_yaxis().set_visible(False)

grid = lab.imshow(data, interpolation='none', cmap='binary')
lab.grid()

cid = fig.canvas.mpl_connect('key_press_event', on_key)
ani = animation.FuncAnimation(fig, step, interval=300)

lab.show()
