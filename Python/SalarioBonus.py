# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 07:59:21 2019
@author: Alexandre Fukaya

URI JUDGE Problem ID 1009
"""

nome    = input();
salario = float(input());
bonus   = float(input()) * 0.15;

print("TOTAL = R$ {0:.2f}".format(salario+bonus))

