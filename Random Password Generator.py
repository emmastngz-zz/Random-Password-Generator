# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 
from tkinter import *

# Characters that can be used in the password
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"

class WritablesStringVar(StringVar):
    
    def write(self, added_text):
        new_text = self.get() + added_text
        self.set(new_text)
        
    def clear(self):
        self.set("")

def password_generator():
    global chars
    
    # Numbers of password to generate
    password_number.get()
    
    # Password lenght 
    password_length.get()
    
    # To avoid the last pack of password
    final_password.clear()
    
    password = ''
    
    try:
        # This for generate a first password
        for p in range(int(password_number.get())):
            # password = ''
            # for nested that generate a password  
            for c in range(int(password_length.get())):
                password += random.choice(chars)
            print(password, file = final_password)
            # To avoid the characters of the last iteration
            password = ''
        
        
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
final_password = WritablesStringVar(root)

# Label password number
pass_num = Label(root, text = "Numbers of Password")
pass_num.pack()
pass_num.config(font = ('times new roman', 12))

# Entry password number
entry_pass_num = Entry(root, justify="center", textvariable = password_number)
entry_pass_num.pack()


# Label password lenght
pass_len = Label(root, text = "Password Lenght")
pass_len.pack()
pass_len.config(font = ('times new roman', 12))

# Entry password number
entry_pass_len = Entry(root, justify="center", textvariable = password_length)
entry_pass_len.pack()


# Label final password
final_pass = Label(root, text = "Password")
final_pass.pack()
final_pass.config(font = ('times new roman', 12))

# Label to show final password
show_passwords = Label(root, justify="center", textvariable = final_password, relief = GROOVE)
show_passwords.pack()


# Create button
gen_pass = Button(root, text = "Generate Password", justify = "center", command = password_generator)
gen_pass.pack()
gen_pass.config(font = ('times new roman', 12))
    
# Main loop 
root.mainloop()