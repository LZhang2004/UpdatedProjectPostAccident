import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import math 
import os 
import time

x = "" #MAIN VARIABLE

def change(*args):
	print(var.get())
	x = var.get()
	print(x)

root = tk.Tk() 


def encrypt():
	x = var.get()

	def finishcaesarencrypt():
		try:
			newword = ""
			y = imput.get("1.0", "end-1c")
			z = entry.get()
			length = len(y) 
			for i in range(0, length, 1):
				quoi = y[i]
				quoi = int(ord(quoi))
				quoi = quoi + int(z)
				quoi = str(chr(quoi))
				newword = newword + quoi
			output.config(state = "normal")
			output.delete('1.0', END)
			output.insert(tk.INSERT, newword)
			output.config(state = "disabled")
			top.destroy()	
		except:
			output.config(state = "normal")
			output.delete('1.0', END)
			output.insert(tk.INSERT, "Error")
			output.config(state = "disabled")

	
	if x == "Caesar Cipher":
		letterchange = 0
		top = Toplevel()
		top.title("instructions")
		instructions = tk.Label(top, text = "How many letters would you like to shift up?")
		instructions.grid(column = 0, row = 0)
		entry = tk.Entry(top)
		entry.grid(column = 0, row = 1)
		submit = tk.Button(top, text = "Submit", command = finishcaesarencrypt, font = ("Arial", 20, "bold"), fg = 'green')
		submit.grid(column = 0, row = 2)
		top.mainloop()




def decrypt():
	x = var.get()

	def finishcaesarencrypt():
		try:
			newword = ""
			y = imput.get("1.0", "end-1c")
			z = entry.get()
			length = len(y) 
			for i in range(0, length, 1):
				quoi = y[i]
				quoi = int(ord(quoi))
				quoi = quoi - int(z)
				quoi = str(chr(quoi))
				newword = newword + quoi
			output.config(state = "normal")
			output.delete('1.0', END)
			output.insert(tk.INSERT, newword)
			output.config(state = "disabled")
			top.destroy()	
		except:
			output.config(state = "normal")
			output.delete('1.0', END)
			output.insert(tk.INSERT, "Error")
			output.config(state = "disabled")
	if x == "Caesar Cipher":
		letterchange = 0
		top = Toplevel()
		top.title("instructions")
		instructions = tk.Label(top, text = "How many letters would you like to shift back?")
		instructions.grid(column = 0, row = 0)
		entry = tk.Entry(top)
		entry.grid(column = 0, row = 1)
		submit = tk.Button(top, text = "Submit", command = finishcaesarencrypt, font = ("Arial", 20, "bold"), fg = 'green')
		submit.grid(column = 0, row = 2)
		top.mainloop()




title = tk.Label(root, text = "Welcome to Encryptor", fg = "black", font = ("Courier", 44) )
title.grid(column = 2, row = 0)

OPTIONS = [
	"Caesar Cipher",
	"Base Conversion",
	"Letter to Number Cipher",
]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.config(height = 3, width = 20)
dropDownMenu.grid(column = 1, row = 1)

def switch():
	yay = encryptlabel.cget("text")
	if yay == "Encrypt":
		encryptlabel.config(text = "Decrypt")
		encrypt.config(text = "Decrypt", command = decrypt)
		switch.config(text = "change to (encrypt)")
	elif yay == "Decrypt":
		encryptlabel.config(text = "Encrypt")
		encrypt.config(text = "Encrypt", command = encrypt)
		switch.config(text = "change to (decrypt)")
	else:
		encryptlabel.config(text = "Encrypt")
		encrypt.config(text = "Encrypt", command = encrypt)
		switch.config(text = "change to (decrypt)")

imput = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
imput.config(state = "normal") # spelled incorrectly because cannot name input
imput.grid(column = 1, row = 2)

encrypt = tk.Button(root, text = "Encrypt", command = encrypt, font = ("Arial", 20, "bold"), fg = 'green')
encrypt.config(height = 3, width = 20)
encrypt.grid(column = 2, row = 2)

switch = tk.Button(root, text = "change to (decrypt)", command = switch, font = ("Arial", 20, "bold"), fg = 'blue')
switch.config(height = 3, width = 20)
switch.grid(column = 2, row = 3)

output = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
output.config(state = "disabled")
output.grid(column = 3, row = 2)

encryptlabel = tk.Label(root, text = "", font = 2, fg = "white")
encryptlabel.grid(column = 0 ,row = 0)



root.mainloop()
