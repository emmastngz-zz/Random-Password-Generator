# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 
from tkinter import *

# Characters that can be used in the password
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"

# Create a dynamic StringVar
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
            # Show the passwords with the dynamic StringVar
            print(password, file = final_password)
            # To avoid the characters of the last iteration
            password = ''
        
        
    except ValueError:
    # If the user type a not int value
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
# pass_num.pack() Never mix grid() and pack() in the same root widget.
pass_num.config(font = ('times new roman', 12))
pass_num.grid(row = 0, column = 0, sticky = W, pady = 2)

# Entry password number
entry_pass_num = Entry(root, justify="center", textvariable = password_number)
# entry_pass_num.pack() Never mix grid() and pack() in the same root widget.
entry_pass_num.grid(row = 1, column = 0, pady = 2)

# Label password lenght
pass_len = Label(root, text = "Password Lenght")
# pass_len.pack() Never mix grid() and pack() in the same root widget.
pass_len.config(font = ('times new roman', 12))
pass_len.grid(row = 0, column = 1, sticky = W, pady = 2)

# Entry password number
entry_pass_len = Entry(root, justify="center", textvariable = password_length)
# entry_pass_len.pack() Never mix grid() and pack() in the same root widget.
entry_pass_len.grid(row = 1, column = 1, pady = 2)

# Label final password
final_pass = Label(root, text = "Password")
# final_pass.pack() Never mix grid() and pack() in the same root widget.
final_pass.config(font = ('times new roman', 12))
final_pass.grid(row = 0, column = 2, sticky = W, pady = 2)

# Label to show final password
show_passwords = Label(root, justify="center", textvariable = final_password, relief = GROOVE)
# show_passwords.pack() Never mix grid() and pack() in the same root widget.
show_passwords.grid(row = 1, column = 2, sticky = W, pady = 2)

# Create button
gen_pass = Button(root, text = "Generate Password", justify = "center", command = password_generator)
# gen_pass.pack() Never mix grid() and pack() in the same root widget.
gen_pass.config(font = ('times new roman', 12))
gen_pass.grid(row = 1, column = 3, sticky = E)
    
# Main loop 
root.mainloop()