# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:53:58 2019

@author: alexandre.fukaya
"""

coord_list = []
n = int(input("Entre com a quantidade de pontos no vetor:"))
for i in range(n):
    print("Entre com as coordenadas do ponto %d " % (i+1))
    x = int(input("X: "))
    y = int(input("Y: "))
    coord_list.append((x, y))

coord_list.sort()

x0, y0 = coord_list[0]
print("(%d,%d) " % (x0, y0))
pontos = 1
for i in range(1, n):
    x1, y1 = coord_list[i]
    if (x0 != x1) and (abs(y0 - y1) >= 2):
        x0 = x1
        y0 = y1
        print("(%d,%d) " % (x0, y0))
        pontos += 1

print(pontos)
