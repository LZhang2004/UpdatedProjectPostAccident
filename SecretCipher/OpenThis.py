import tkinter as tk
from tkinter import *
import math
import os


root = tk.Tk()
root.title("SecretCipher")

title = tk.Label(root, text = "Welcome to SecretCipher", fg = "black", width = "200")
title.config(font=("Courier", 44))
title.pack()


def InitiateGame():
	root.destroy()
	import MainGame

def InitiateEncryptor(): 
	root.destroy()
	import Encryptor


btn1 = tk.Button(root, text = "Game", command = InitiateGame)
btn1.config(height = 10, width = 50)
btn1.pack()

btn2 = tk.Button(root, text = "Encryptor", command = InitiateEncryptor)
btn2.config(height = 10, width = 50)
btn2.pack()

root.mainloop()