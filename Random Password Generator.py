# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"
number = int(input('Numbers of password?: '))

lenght = int(input('Password lenght?: '))

for p in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)