# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:07:27 2020

@author: Emmanuel
"""

import tkinter as tk

class WritableStringVar(tk.StringVar):
    def write(self, added_text):
        new_text = self.get() + added_text
        self.set(new_text)

    def clear(self):
        self.set("")
                 
root = tk.Tk()

textvar = WritableStringVar(root)

label = tk.Label(root, textvariable=textvar)
label.pack()

for i in range(4):
    print("hello there", file=textvar)

root.mainloop()