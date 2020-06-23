# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 
from tkinter import *


# Characters that can be used in the password
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"


def password_generator():
    global chars
    
    # Numbers of password to generate
    password_number.get()
    
    # Password lenght 
    password_length.get()
    
    password = ''
    
    try:
        # This for generate a first password
        for p in range(int(password_number.get())):
            # password = ''
            # for nested that generate a password  
            for c in range(int(password_length.get())):
                password += random.choice(chars)
            password += '\n\n'
        # To set password
        final_password.set(password)
        
    except ValueError:
       messages =  Label(root, text = "Error!: please type a integer number")
       messages.pack()
       messages.config(fg = "red", font = ('times new roman', 12, 'bold'))
    
# Setup root
root = Tk()
root.title("Random Password Generator")
root.iconbitmap('ink-bottle-and-a-feather-to-write_icon-icons.com_56812.ico')
    
# Variables
password_number = StringVar()
password_length = StringVar()
final_password = StringVar()

# Label password number
pass_num = Label(root, text = "Numbers of Password")
pass_num.pack()
pass_num.config(font = ('times new roman', 12))
Entry(root, justify="center", textvariable = password_number).pack()

# Label password lenght
pass_len = Label(root, text = "Password Lenght")
pass_len.pack()
pass_len.config(font = ('times new roman', 12))
Entry(root, justify="center", textvariable = password_length).pack()

# Label final password
final_pass = Label(root, text = "Password")
final_pass.pack()
final_pass.config(font = ('times new roman', 12))
Entry(root, justify="center", text = final_password, state = "disabled").pack()

# Create button
gen_pass = Button(root, text = "Generate Password", justify = "center", command = password_generator)
gen_pass.pack()
gen_pass.config(font = ('times new roman', 12))
    
# Main loop 
root.mainloop()