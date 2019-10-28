# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:45:18 2019

@author: alexandre.fukaya
URI JUDGE Problem ID 1008
"""

empID  = input()
hours  = int(input())
vHours = float(input())

salary = hours * vHours

print('NUMBER = {0}'.format(empID))
print('SALARY = U$ {0:.2f}'.format(salary))
