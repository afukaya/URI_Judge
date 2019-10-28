# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:52:49 2019

@author: Alexandre Fukaya
URI JUDGE Problem ID 1026
"""

v1 = int(input())
v2 = int(input())

bin1 = format(v1,'032b') 
bin2 = format(v2,'032b')
bin3 = []

for i in range(31,0,-1):
    a = int(bin1[i])
    b = int(bin2[i])
    gAnd1  = ~a & b
    gAnd2  = ~b & a
    gCarry = a & b
    gSum   = gAnd1 | gAnd2
    bin3.append(gSum)
bin3.reverse()
out = ''
for s in bin3:
    out += str(s)

print(format(out,'d'))
#bin3 = str(bin3).strip(',')
#print(bin3)

#print(format(bin3,'d'))