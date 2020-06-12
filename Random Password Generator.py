# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 

# Characters that can be used in the password
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"
# Numbers of password to generate
number = int(input('Numbers of password?: '))

# Password lenght 
lenght = int(input('Password lenght?: '))

# This for generate a first password
for p in range(number):
    password = ''
    # for nested that generate a password  
    for c in range(lenght):
        password += random.choice(chars)
    # To show password
    print(password)
    
