# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:47:16 2019

@author: Alexandre Fukaya
URI JUDGE Problem ID 1010
"""
v1 = input().split(" ")
v2 = input().split(" ")

cod1 = int(v1[0])
qtd1 = int(v1[1])
val1 = float(v1[2])
tot1 = qtd1 * val1

cod2 = int(v2[0])
qtd2 = int(v2[1])
val2 = float(v2[2])
tot2 = qtd2 * val2

tot = tot1 + tot2

print("VALOR A PAGAR: R$ {0:.2f}".format(tot))
