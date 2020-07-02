# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:23 2020

@author: Emmanuel
"""
import random 
from tkinter import *
import sqlite3

# Characters that can be used in the password
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#~€¬/"

# Object to show messages
messages_notice = ''

# List for passwords
passwords_list = []


# Create a dynamic StringVar
class WritablesStringVar(StringVar):
    
    def write(self, added_text):
        new_text = self.get() + added_text
        self.set(new_text)
        
    def clear(self):
        self.set("")

def password_generator():
    
    global chars
    
    global messages_notice
    
    global passwords_list
    
    # Numbers of password to generate
    password_number.get()
    
    # Password lenght 
    password_length.get()
    
    # To avoid the last pack of password
    final_password.clear()
    
    # Clean password variable
    password = ''
    
    # Clean passwords list 
    passwords_list = []
    
    try:
        # This for generate a first password
        for p in range(int(password_number.get())):
            # password = ''
            # for nested that generate a password  
            for c in range(int(password_length.get())):
                password += random.choice(chars)
            # Show the passwords with the dynamic StringVar
            print(password, file = final_password)
            passwords_list.append(password)
            # To avoid the characters of the last iteration
            password = ''
        
        
    except ValueError:
    # If the user type a not int value
       messages_notice =  Label(root, text = "Error!: please type a integer number")
       # messages.pack() Never mix grid() and pack() in the same root widget.
       messages_notice.config(fg = "red", font = ('times new roman', 12, 'bold'))
       messages_notice.grid(row = 2, column = 0, sticky = W)
    

# Setup data base
def create_bd():
    
    global messages_notice
    
    connection = sqlite3.connect("password_final.db") 
    cursor = connection.cursor()
    
    try:
        cursor.execute('''
                       CREATE TABLE passwords(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           pass VARCHAR(100) UNIQUE NOT NULL)
                       ''')
                       
    except sqlite3.OperationalError:
        messages_notice = Label(root, text = "Data base has already been created")
        messages_notice.config(fg = "red", font = ('times new roman', 12, 'bold'))
        messages_notice.grid(row = 2, column = 0, sticky = W)
        
    else:
        messages_notice = Label(root, text = "Data base has benn created")
        messages_notice.config(fg= "red", font = ('times new roman', 12, 'bold'))
        messages_notice.grid(row = 2, column = 0, sticky = W)
        
    connection.close()
    
    
# Save data base
def save_data_base():
    
    global messages_notice
    global passwords_list
    
    connection = sqlite3.connect("password_final.db")
    cursor = connection.cursor()
    
    # Save passwords from the list
    try: 
        for password in passwords_list:   
            cursor.execute("INSERT INTO passwords VALUES (null, '{}')".format(str(password)))
    
    except:
        messages_notice = Label(root, text = "Error! the passwords can't be saves")
        messages_notice.config(fg= "red", font = ('times new roman', 12, 'bold'))
        messages_notice.grid(row = 2, column = 0, sticky = W)
    else:
        messages_notice = Label(root, text = "passwords saved successfully")
        messages_notice.config(fg= "red", font = ('times new roman', 12, 'bold'))
        messages_notice.grid(row = 2, column = 0, sticky = W)
       
    connection.commit()
    connection.close()
        
        
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

# Save button
save_button = Button(root, text = "Save Password", justify = "center", command = save_data_base)
save_button.config(font = ('times new roman', 12))
save_button.grid(row = 1, column = 4, sticky = E)

# Create data base
create_bd()

# Main loop 
root.mainloop()