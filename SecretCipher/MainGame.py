#main game
#http://jjal.download/index.php?module=sms&lang=en - Phone Notification Fake all going to use this for the messages
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import math 
import os 
import time

'''
IDEAS 
1) Sound effects
2) Animations 
3) Soundtrack? 
4) Visual Effect?
'''



root = tk.Tk()
root.title("Game")

def kill():
	root.destroy()

def encryptoropen():
	import Encryptor.py

#enable and disable keypad and message buttons
def enableMessage(): 
	messagebutton.config(state = "normal")

def enableKeypad(): 
	keypadbutton.config(state = "normal")

def useless():
	storyline.insert(tk.INSERT, "")

def plusone(int):
	if int >=10:
		return 0
	else:
		return int + 1

def minusone(int):
	if int <= 0:
		return 10
	else:
		return int - 1

def colors():

	def blue():
		def black():
			def green():
				def red():

					def blacknwhite():
						root.config(bg = "black")

					root.config(bg = "red")
					root.after(200, blacknwhite)

				root.config(bg = "green")
				root.after(200, red)			

			root.config(bg = "black")
			root.after(200, green)

		root.config(bg = "blue")
		root.after(200, black)

	root.config(bg = "red")
	root.after(200, blue)



username = "username"


def backdoor():
	root.after(10, finishlevel2state)


#The text box for the story (Begin)
def StoryBegin():
	storyline.config(state = "normal")
	storyline.insert(tk.INSERT, "\nSecretCipher : By Leo Zhang")
	storyline.insert(tk.INSERT,"\nVersion 1.0.4")
	storyline.insert(tk.INSERT,"\nEntering....")
	storyline.insert(tk.INSERT,"\nThis is the tutorial!!!")
	storyline.insert(tk.INSERT,"\nYou are in the enemy base")
	storyline.insert(tk.INSERT,"\nYou need to get into the office...")
	storyline.insert(tk.INSERT,"\nThere is a number lock on the door...")
	storyline.insert(tk.INSERT,"\nYou got a message on your phone!...")
	storyline.insert(tk.INSERT,"\nPress Recieve Message when done reading this!")
	root.after(1000, enableMessage) 
	storyline.config(state = "disabled")
	beginbutton.config(command = useless)

#The tutorial box - just a gray frame
def display_tutorial_password(): 
	top = Toplevel(visual = "truecolor")
	top.title("PhoneMessage") #http://jjal.download/index.php?module=sms&lang=en
	top.configure(background='grey')

#The function to destroy the username thing, show photo, and disable username box and enable input password, set command for the messages button to #2
	def please(): 
		n = str(entr.get())
		username = n
		path = "/Users/"+n+"/Desktop/Git_Repo/Year9DesignCS-PythonLZ-master/SecretCipher/Images/tutorial_password.png"
		img = ImageTk.PhotoImage(Image.open(path))
		panel = tk.Label(top, image = img)
		panel.grid(column = 0, row = 0)
		btn1.destroy()
		title.destroy()
		entr.destroy()
		title2.destroy()
		message = tk.Label(top, text = "After you have read this, click the red button in the top left corner", fg = "black", font = ("Courier", 20) )
		message.grid(column = 0, row = 1)
		message2 = tk.Label(top, text = "and you can now click the <enter password> button on the right of the window", fg = "black", font = ("Courier", 20) )
		message2.grid(column = 0, row = 2)
		username = n
		messagebutton.config(state = "disabled", command = Upstairs)
		messagebutton.config(text = "Proceed")
		keypadbutton.config(state = "normal")
		usernamelabel.config(text = n)
		top.mainloop()
	# the input username box - so all computers can use
	title = tk.Label(top, text = "Please input your computer username for this to work (example - leo.zhang)", fg = "black", font = ("Courier", 20) )
	title.grid(column = 0, row = 0)
	title2 = tk.Label(top, text = "If nothing happens, the username is incorrect", fg = "black", font = ("Courier", 20) )
	title2.grid(column = 0, row = 1)
	btn1 = tk.Button(top, text = "Submit", command = please, font = ("Arial", 20, "bold"), fg = 'red')
	btn1.config(height = 3, width = 10)
	btn1.grid(column = 0, row = 4)
	entr = tk.Entry(top)
	entr.grid(column = 0, row = 3)
	n = str(entr.get())
	username = n
	
#keypad frame for tutorial input	
def keypad1(): 
	top = Toplevel()
	top.title("keypad1")
	#function to check the input
	def check(): 
		n = int(entr.get())

		#function to close keypad, refresh storyline text, enable level 1, turn begin to green
		def please2():
				top.destroy()
				messagebutton.config(state = "disabled")
				keypadbutton.config(state = "disabled")
				beginbutton.config(fg = 'green', command = useless)
				level1button.config(state = "normal")
				storyline.config(state = "normal")
				storyline.delete('1.0', END)
				storyline.insert(tk.INSERT, "Congrats on completing the tutorial!!!")
				storyline.insert(tk.INSERT, "\nClick Level 1 to continue :)")
				storyline.config(state = "disabled")
				title.config(text = "Level 1")
				top.mainloop()
		#continuing the check if answer is right
		if n == 9832:
			title3.config(text = "Status: CORRECT! Wait 3 seconds for continue", fg = "green")
			top.after(2000, please2)
		elif n == 666:
			top.after(100, backdoor)
		else: 
			title3.config(text = "Status: INCORRECT! Please Try Again", fg = "red")
	#frame for the keypad 
	title2 = tk.Label(top, text = "Enter the Password", fg = "black", font = ("Courier", 20) )
	title2.grid(column = 0, row = 0)
	entr = tk.Entry(top)
	entr.grid(column = 0, row = 1)
	btn1 = tk.Button(top, text = "Submit", command = check, font = ("Arial", 20, "bold"), fg = 'red')
	btn1.config(height = 3, width = 10)
	btn1.grid(column = 0, row = 2)
	title3 = tk.Label(top, text = "Status: Password not entered", fg = "black", font = ("Courier", 30) )
	title3.grid(column = 0, row = 3)





















def LevelOne(): 
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT,"\nCongrats on completing the tutorial btw :) ")
	storyline.insert(tk.INSERT,"\nNow, you're in the building")
	storyline.insert(tk.INSERT,"\nWhat do you do now?")
	storyline.insert(tk.INSERT,"\nClick on the PROCEED button to continue")
	root.after(1000, enableMessage) 
	storyline.config(state = "disabled")	
	level1button.config(command = useless)


def Upstairs():
	messagebutton.config(text = "Recieve Message")
	keypadbutton.config(command = keypadtutorial)
	messagebutton.config(state = "disabled")
	keypadbutton.config(state = "normal")
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT,"\nThere is a Lock on the Door!")
	storyline.insert(tk.INSERT,"\nThere is a paper taped beside the keypad")
	storyline.insert(tk.INSERT,"\nIt says {The password is 442 in base 8}")	
	#the answer is 672
	storyline.insert(tk.INSERT,"\nYou need to convert the number 442 into Base 8 for the password")	
	storyline.insert(tk.INSERT,"\nWhen you are ready, press the input")
	storyline.insert(tk.INSERT,"\npassword button!")
	storyline.config(state = "disabled")


def keypadtutorial():
	kpt = Toplevel()
	kpt.title("keypad Tutorial")

	def EndMe():
		kpt.destroy()
		kpt.after(100, keypad2a)

	gotokeypad = tk.Button(kpt, text = "PROCEED", fg = 'black', font = ("Arial", 60, "bold"), command = EndMe)
	gotokeypad.grid(column = 1, row = 2)
	instructions = tk.Label(kpt, text = "This is the key-lock tutorial. Press buttons on either side of each number" + 
		" to make the number go higher or lower. Enter the numbers in order from top to bottom. ")
	instructions.grid(column = 1, row = 0)
	username = usernamelabel.cget("text")
	path = "/Users/"+username+"/Desktop/Git_Repo/Year9DesignCS-PythonLZ-master/SecretCipher/Images/baseconversion.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(kpt, image = img)
	panel.grid(column = 1, row = 1)

	kpt.mainloop()


def keypad2a():
	lock = Toplevel()
	lock.title("Lock")
	attempt1 = Frame(lock, cursor = "dot")
	attempt1.grid(column = 0, row = 1)
	label = tk.Label(lock, font = ("Arial", 20, "bold"), text = "Remember, convert 442 into base 8")
	label.grid(column = 0, row = 0)
	locknumber1 = 0
	label2 = 0
	label3= 0 
	please1 = 0

	def left1():
		locknumber1 = int(Label1.cget("text"))
		locknumber1 = minusone(locknumber1)
		Label1.config(text = locknumber1)
	
	def right1():
		locknumber1 = int(Label1.cget("text"))
		locknumber1 = plusone(locknumber1)
		Label1.config(text = locknumber1)

	def left2():
		label2 = int(Label2.cget("text"))
		label2 = minusone(label2)
		Label2.config(text = label2)

	def right2():
		label2 = int(Label2.cget("text"))
		label2 = plusone(label2)
		Label2.config(text = label2)

	def left3():
		label3 = int(Label3.cget("text"))
		label3 = minusone(label3)
		Label3.config(text = label3)

	def right3():	
		label3 = int(Label3.cget("text"))
		label3 = plusone(label3)
		Label3.config(text = label3)


	def check():

		def endlevel1():
			lock.destroy()
			btn4.config(state = "normal")
			level1button.config(command = useless, fg = "green")
			keypadbutton.config(state = "disabled")
			storyline.config(state = "normal")
			storyline.delete('1.0', END)
			storyline.insert(tk.INSERT, "Congrats on completing LEVEL 1!!! :) :) :) ")
			storyline.insert(tk.INSERT, "\nClick Level 2 to continue")
			storyline.config(state = "disabled")
			title.config(text = "Level 2")



		#the password is 672
		label3 = int(Label3.cget("text"))
		locknumber1 = int(Label1.cget("text"))
		label2 = int(Label2.cget("text"))
		if locknumber1 == 6 and label2 == 7 and label3 == 2:
			yesorno.config(text = "THE PASSWORD IS CORRECT", fg = "green")
			lock.after(2000, endlevel1)
		else:
			yesorno.config(text = "THE PASSWORD IS INCORRECT", fg = "red")



	left1 = tk.Button(attempt1, text = "<<<<-----", command = left1)
	left1.grid(column = 0, row = 0)
	right1 = tk.Button(attempt1, text = "----->>>>", command =right1)
	right1.grid(column = 3, row = 0)
	Label1 = tk.Label(attempt1, text = str(locknumber1))
	Label1.grid(column = 2, row = 0)
	left2 = tk.Button(attempt1, text = "<<<<-----", command = left2)
	left2.grid(column = 0, row = 1)
	right2 = tk.Button(attempt1, text = "----->>>>", command = right2)
	right2.grid(column = 3, row = 1)
	Label2 = tk.Label(attempt1, text = str(label2))
	Label2.grid(column = 2, row = 1)
	left3 = tk.Button(attempt1, text = "<<<<-----", command = left3)
	left3.grid(column = 0, row = 2)
	right3 = tk.Button(attempt1, text = "----->>>>", command = right3)
	right3.grid(column = 3, row = 2)
	Label3 = tk.Label(attempt1, text = str(label3))
	Label3.grid(column = 2, row = 2)
	submit = tk.Button(attempt1, text = "SUBMIT", fg = 'black', font = ("Arial", 20, "bold"), command = check)
	submit.grid(column = 2, row = 3)
	yesorno = tk.Label(attempt1, text = ("Password: Not submitted yet"))
	yesorno.grid(column = 2, row = 4)
	lock.mainloop()















def LevelTwo(): 
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT, "\nCongrats on getting this far!!")
	storyline.insert(tk.INSERT,"\nYou find the door to the control room.....")
	storyline.insert(tk.INSERT,"\nBUT THERE'S ANOTHER LOCK")
	storyline.insert(tk.INSERT,"\nProceed?")
	root.after(1000, Proceed) 
	storyline.config(state = "disabled")

def Proceed():
	messagebutton.config(state = "normal", text = "Proceed", command = LevelTwoA)

def LevelTwoA():
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT, "\n!!Message Recieved!!")
	storyline.insert(tk.INSERT,"\nCheck?")
	storyline.config(state = "disabled")
	messagebutton.config(text = "Check Message", command = anothermessage)
	btn4.config(command = useless)


def anothermessage():
	qq = Toplevel()
	qq.title("keypad Tutorial")

	def EndMe2():
		qq.destroy()
		qq.after(100, keepongoing2)

	gotokeypad = tk.Button(qq, text = "OKAY", fg = 'black', font = ("Arial", 60, "bold"), command = EndMe2)
	gotokeypad.grid(column = 1, row = 2)
	instructions = tk.Label(qq, text = "This is the key-lock tutorial. Press buttons on either side of each number" + 
		" to make the number go higher or lower. Enter the numbers in order from top to bottom. ")
	instructions.grid(column = 1, row = 0)
	username = usernamelabel.cget("text")
	path = "/Users/"+username+"/Desktop/Git_Repo/Year9DesignCS-PythonLZ-master/SecretCipher/Images/passwordlevel2.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = tk.Label(qq, image = img)
	panel.grid(column = 1, row = 1)

	qq.mainloop()

def keepongoing2():
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT, "\nEnter the password!")
	storyline.config(state = "disabled")
	messagebutton.config(state = "disabled")
	keypadbutton.config(command = keypad2please, state = "normal")


def keypad2please():
	ww = Toplevel()
	ww.title("KEYPOAD")

	def check():

		input = text.get("1.0", "end-1c")
		if input == "PASSWORD":
			ww.config(bg = "green")
			ww.after(1000, finishlevel2state)
			text.config(state = "normal")
			text.delete('1.0', END)
			text.insert(tk.INSERT, "Click the red close button in the top left")
			text.config(state = "disabled")
		else:
			ww.config(bg = "red")

	def refresh():
		text.config(state = "normal")
		text.delete('1.0', END)
		text.config(state = "disabled")


	def addA():
		text.config(state = "normal")
		text.insert(tk.INSERT, "A")
		text.config(state = "disabled")

	def addB():
		text.config(state = "normal")
		text.insert(tk.INSERT, "B")
		text.config(state = "disabled")

	def addC():
		text.config(state = "normal")
		text.insert(tk.INSERT, "C")
		text.config(state = "disabled")

	def addD():
		text.config(state = "normal")
		text.insert(tk.INSERT, "D")
		text.config(state = "disabled")

	def addE():
		text.config(state = "normal")
		text.insert(tk.INSERT, "E")
		text.config(state = "disabled")


	def addF():
		text.config(state = "normal")
		text.insert(tk.INSERT, "F")
		text.config(state = "disabled")

	def addG():
		text.config(state = "normal")
		text.insert(tk.INSERT, "G")
		text.config(state = "disabled")		

	def addH():
		text.config(state = "normal")
		text.insert(tk.INSERT, "H")
		text.config(state = "disabled")

	def addI():
		text.config(state = "normal")
		text.insert(tk.INSERT, "I")
		text.config(state = "disabled")

	def addJ():
		text.config(state = "normal")
		text.insert(tk.INSERT, "J")
		text.config(state = "disabled")

	def addK():
		text.config(state = "normal")
		text.insert(tk.INSERT, "K")
		text.config(state = "disabled")

	def addL():
		text.config(state = "normal")
		text.insert(tk.INSERT, "L")
		text.config(state = "disabled")

	def addM():
		text.config(state = "normal")
		text.insert(tk.INSERT, "M")
		text.config(state = "disabled")

	def addN():
		text.config(state = "normal")
		text.insert(tk.INSERT, "N")
		text.config(state = "disabled")

	def addO():
		text.config(state = "normal")
		text.insert(tk.INSERT, "O")
		text.config(state = "disabled")


	def addP():
		text.config(state = "normal")
		text.insert(tk.INSERT, "P")
		text.config(state = "disabled")

	def addQ():
		text.config(state = "normal")
		text.insert(tk.INSERT, "Q")
		text.config(state = "disabled")

	def addR():
		text.config(state = "normal")
		text.insert(tk.INSERT, "R")
		text.config(state = "disabled")

	def addS():
		text.config(state = "normal")
		text.insert(tk.INSERT, "S")
		text.config(state = "disabled")

	def addT():
		text.config(state = "normal")
		text.insert(tk.INSERT, "T")
		text.config(state = "disabled")

	def addU():
		text.config(state = "normal")
		text.insert(tk.INSERT, "U")
		text.config(state = "disabled")

	def addV():
		text.config(state = "normal")
		text.insert(tk.INSERT, "V")
		text.config(state = "disabled")

	def addW():
		text.config(state = "normal")
		text.insert(tk.INSERT, "W")
		text.config(state = "disabled")

	def addX():
		text.config(state = "normal")
		text.insert(tk.INSERT, "X")
		text.config(state = "disabled")

	def addY():
		text.config(state = "normal")
		text.insert(tk.INSERT, "Y")
		text.config(state = "disabled")

	def addZ():
		text.config(state = "normal")
		text.insert(tk.INSERT, "Z")
		text.config(state = "disabled")



	gotokeypad = tk.Button(ww, text = "SUBMIT", fg = 'black', font = ("Arial", 20, "bold"), command = check)
	gotokeypad.grid(column = 5, row = 5)

	text = tk.Text(ww, width = 50, height = 3, borderwidth = 3, relief = tk.GROOVE)
	text.config(state = "disabled")
	text.grid(column = 5, row = 1)

	refresh = tk.Button(ww, text = " refresh", command = refresh)
	refresh.grid(column = 6, row = 6)

	btnA = tk.Button(ww, text = "A", font = ("Arial", 20, "bold"), fg = 'red', command = addA)
	btnA.grid(column = 0, row = 1)

	btnB = tk.Button(ww, text = "B", font = ("Arial", 20, "bold"), fg = 'red', command = addB)
	btnB.grid(column = 1, row = 1)

	btnC = tk.Button(ww, text = "C", font = ("Arial", 20, "bold"), fg = 'red', command = addC)
	btnC.grid(column = 2, row = 1)

	btnD = tk.Button(ww, text = "D", font = ("Arial", 20, "bold"), fg = 'red', command = addD)
	btnD.grid(column = 3, row = 1)

	btnE = tk.Button(ww, text = "E", font = ("Arial", 20, "bold"), fg = 'red', command = addE)
	btnE.grid(column = 4, row = 1)

	btnF = tk.Button(ww, text = "F", font = ("Arial", 20, "bold"), fg = 'red', command = addF)
	btnF.grid(column = 0, row = 2)

	btnG = tk.Button(ww, text = "G", font = ("Arial", 20, "bold"), fg = 'red', command = addG)
	btnG.grid(column = 1, row = 2)

	btnH = tk.Button(ww, text = "H", font = ("Arial", 20, "bold"), fg = 'red', command = addH)
	btnH.grid(column = 2, row = 2)

	btnI = tk.Button(ww, text = "I", font = ("Arial", 20, "bold"), fg = 'red', command = addI)
	btnI.grid(column = 3, row = 2)

	btnJ = tk.Button(ww, text = "J", font = ("Arial", 20, "bold"), fg = 'red', command = addJ)
	btnJ.grid(column = 4, row = 2)

	btnK = tk.Button(ww, text = "K", font = ("Arial", 20, "bold"), fg = 'red', command = addK)
	btnK.grid(column = 0, row = 3)

	btnL = tk.Button(ww, text = "L", font = ("Arial", 20, "bold"), fg = 'red', command = addL)
	btnL.grid(column = 1, row = 3)

	btnM = tk.Button(ww, text = "M", font = ("Arial", 20, "bold"), fg = 'red', command = addM)
	btnM.grid(column = 2, row = 3)

	btnN = tk.Button(ww, text = "N", font = ("Arial", 20, "bold"), fg = 'red', command = addN)
	btnN.grid(column = 3, row = 3)

	btnO = tk.Button(ww, text = "O", font = ("Arial", 20, "bold"), fg = 'red', command = addO)
	btnO.grid(column = 4, row = 3)

	btnP = tk.Button(ww, text = "P", font = ("Arial", 20, "bold"), fg = 'red', command = addP)
	btnP.grid(column = 0, row = 4)

	btnQ = tk.Button(ww, text = "Q", font = ("Arial", 20, "bold"), fg = 'red', command = addQ)
	btnQ.grid(column = 1, row = 4)

	btnR = tk.Button(ww, text = "R", font = ("Arial", 20, "bold"), fg = 'red', command = addR)
	btnR.grid(column = 2, row = 4)

	btnS = tk.Button(ww, text = "S", font = ("Arial", 20, "bold"), fg = 'red', command = addS)
	btnS.grid(column = 3, row = 4)

	btnT = tk.Button(ww, text = "T", font = ("Arial", 20, "bold"), fg = 'red', command = addT)
	btnT.grid(column = 4, row = 4)

	btnU = tk.Button(ww, text = "U", font = ("Arial", 20, "bold"), fg = 'red', command = addU)
	btnU.grid(column = 0, row = 5)

	btnV = tk.Button(ww, text = "V", font = ("Arial", 20, "bold"), fg = 'red', command = addV)
	btnV.grid(column = 1, row = 5)

	btnW = tk.Button(ww, text = "W", font = ("Arial", 20, "bold"), fg = 'red', command = addW)
	btnW.grid(column = 2, row = 5)

	btnX = tk.Button(ww, text = "X", font = ("Arial", 20, "bold"), fg = 'red', command = addX)
	btnX.grid(column = 3, row = 5)

	btnY = tk.Button(ww, text = "Y", font = ("Arial", 20, "bold"), fg = 'red', command = addY)
	btnY.grid(column = 4, row = 5)

	btnZ = tk.Button(ww, text = "Z", font = ("Arial", 20, "bold"), fg = 'red', command = addZ)
	btnZ.grid(column = 0, row = 6)






def finishlevel2state():
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT, "\n GOOD JOB! FINAL TASK UP AHEAD")
	storyline.insert(tk.INSERT, "\n JUST CLICK LEVEL 3!")
	storyline.config(state = "disabled")
	keypadbutton.config(state = "disabled")
	btn4.config(fg = "green", command = useless, state = "normal")
	messagebutton.config(command = purge, state = "disabled")
	storyline.config(state = "disabled")
	title.config(text = "FINAL LEVEL")
	btn6.config(state = "normal", command = purge)

	beginbutton.config(fg = "green", command = useless, state = "normal")
	level1button.config(fg = "green", command = useless, state = "normal")












#LEVEL THREE
def purge():
	title.destroy()
	beginbutton.destroy()
	level1button.destroy()
	btn4.destroy()
	btn6.destroy()
	storyline.destroy()
	messagebutton.destroy()
	keypadbutton.destroy()
	usernamelabel.destroy()
	root.geometry("1200x700")
	firstfinal = tk.Button(root, text = "Lets Begin The Final Test", command = beginthedeath, font = ("Arial", 20, "bold"), fg = 'black')
	firstfinal.grid(column = 0, row = 0)
	firstfinal.place(relx=0.5, rely=0.5, anchor=CENTER)
	root.after(100, colors)




def beginthedeath():
	x = 3
	def right():
		btnD.config(fg = "green")
		deathattempts.config(text = "VICTORY - GOING TO ENCRYPTOR", font = 100, fg = "green")
		root.after(2000, encryptoropen)
		root.after(3000, kill)

	def wrong():
		for i in range(1, 2, 1):
			try:
				x = int(deathattempts.cget("text"))
				deathattempts.config(text = "3", fg = "red", font = ("Arial", 200, "bold"))
				x = minusone(x)
				deathattempts.config(text = x)
				if x == 0:
					deathattempts.config(text = "You have Failed", font = 100)
					root.after(3000, kill)
			except:
				deathattempts.config(text = "3")


	deathattempts = tk.Label(root, text = "I WILL COUNT UP WHEN YOU GET THINGS WRONG, ONE OF THE BUTTONS UNLOCKS THE ENCRYPTOR", fg = "red", bg = "black", font = ("Arial", 20, "bold"))
	deathattempts.grid(column = 0, row = 1)
	deathattempts.place(relx=0.5, rely=0.5, anchor=CENTER)

	btnD = tk.Button(root, text = "E", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnD.config(height = 3, width = 10)
	btnD.grid(column = 0, row = 0)

	btnG = tk.Button(root, text = "G", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnG.config(height = 3, width = 10)
	btnG.grid(column = 1, row = 0)

	btnQ = tk.Button(root, text = "Q", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnQ.config(height = 3, width = 10)
	btnQ.grid(column = 2, row = 0)

	btnJ = tk.Button(root, text = "J", command = right, fg = "red", font = ("Arial", 20, "bold"))
	btnJ.config(height = 3, width = 10)
	btnJ.grid(column = 3, row = 0)

	btnV = tk.Button(root, text = "V", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnV.config(height = 3, width = 10)
	btnV.grid(column = 4, row = 0)

	btnP = tk.Button(root, text = "P", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnP.config(height = 3, width = 10)
	btnP.grid(column = 5, row = 0)

	btnK = tk.Button(root, text = "K", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnK.config(height = 3, width = 10)
	btnK.grid(column = 6, row = 0)

	btnM = tk.Button(root, text = "M", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnM.config(height = 3, width = 10)
	btnM.grid(column = 7, row = 0)

	btnL = tk.Button(root, text = "L", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnL.config(height = 3, width = 10)
	btnL.grid(column = 8, row = 0)

	btnR = tk.Button(root, text = "R", command = wrong, fg = "red", font = ("Arial", 20, "bold"))
	btnR.config(height = 3, width = 10)
	btnR.grid(column = 9, row = 0)








#Title Label
title = tk.Label(root, text = "Welcome to the Game", fg = "black", font = ("Courier", 44) )
title.grid(column = 2, row = 0)

#Begin
beginbutton = tk.Button(root, text = "Begin", command = StoryBegin, font = ("Arial", 20, "bold"), fg = 'red')
beginbutton.config(height = 3, width = 10)
beginbutton.grid(column = 2, row = 1)

#Level buttons
level1button = tk.Button(root, text = "Level 1", font = ("Arial", 20, "bold"), command = LevelOne, state = "disabled", fg = 'red')
level1button.config(height = 3, width = 10)
level1button.grid(column = 0, row = 2)

btn4 = tk.Button(root, text = "Level 2", command = LevelTwo, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn4.config(height = 3, width = 10)
btn4.grid(column = 2, row = 2)

btn6 = tk.Button(root, text = "Level 3", command = purge, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn6.config(height = 3, width = 10)
btn6.grid(column = 3, row = 2)

#text box
storyline = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
storyline.config(state = "disabled")
storyline.grid(column = 2, row = 3)

#display message button and display keypad button
messagebutton = tk.Button(root, text = "Recieve Message", command = display_tutorial_password, font = ("Arial", 20, "bold"), fg = 'green', state = "disabled")
messagebutton.config(height = 3, width = 20)
messagebutton.grid(column = 2, row = 5)

keypadbutton = tk.Button(root, text = "Enter Password", command = keypad1, font = ("Arial", 20, "bold"), fg = 'green', state = "disabled")
keypadbutton.config(height = 3, width = 20)
keypadbutton.grid(column = 3, row = 3)

usernamelabel = tk.Label(root, text = "")
usernamelabel.grid(column = 3, row = 5)




root.mainloop()