try:
    # Python27
    import Tkinter as tk
    import ttk
    from Tkinter import *
    from tkMessageBox import showinfo, showwarning, showerror
except ImportError:
    # Python31+
    import tkinter as tk
    import tkinter.ttk as ttk
from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry
from ttk import *
import tkMessageBox
import webbrowser
from tkMessageBox   import askquestion, showerror,askyesno

buttons = []
v = 0
entry = []
txt =""

def getvalbycol(s):
    if s == "red":
	return 0
    elif s == "green":
        return 1
    elif s == "blue":
	return 2
    else:
	return 3

def getcolbyval(s):
    if s == 0:
	return "red"
    elif s == 1:
        return "green"
    elif s == 2:
	return "blue"
    else:
	return "purple"


def pressed(i,j):
    global txt
    txt = "["+str(i)+", "+str(j)+"]"
    entry.insert(0,txt)
    for k in range(7):	
	back = buttons[i*7 + k].cget('bg')
	if back == "red":
		buttons[i*7 + k].configure(text = "1", bg = "green")	
	elif back == "green":
		buttons[i*7 + k].configure(text = "2", bg = "blue")
	elif back == "blue":
		buttons[i*7 + k].configure(text = "3", bg = "purple")
	else:
		buttons[i*7 + k].configure(text = "0", bg = "red")
    for k in range(7):
		if(k!=i):
			back = buttons[k*7 + j].cget('bg')
			if back == "red":
				buttons[k*7 + j].configure(text = "1", bg = "green")	
			elif back == "green":
				buttons[k*7 + j].configure(text = "2", bg = "blue")
			elif back == "blue":
				buttons[k*7 + j].configure(text = "3", bg = "purple")
			else:
				buttons[k*7 + j].configure(text = "0", bg = "red")

    

def web():
    if tkMessageBox.askyesno('Redirecting to Alien Tiles home page', '\nContinue?'):
    	webbrowser.open("http://www.alientiles.com/")

def restart():
    color = v.get()
    print color
    t = getvalbycol(color)
    for i in range(49):
		buttons[i].configure(text = t, bg = color)	


def main():
    DEFAULTVALUE_OPTION = 'Restart (choose color from list)'
    root = Tk() 
    root.title('Lets Play Alien Tiles!')
    root.geometry('478x340') 
    root.configure(background='black')
    row = 1
    global buttons
    for i in range(7):
	for j in range(7):
		b = tk.Button(text="0",command= lambda x1=i, y1=j: pressed(x1,y1), bg = 'red', width=5)
		b.grid(row = i, column = j)
		buttons.append(b)
    pattern = tk.Label(text="Pattern")
    pattern.grid( row = 8, column = 2, columnspan=3, sticky=W+E)
    global entry
    entry = tk.Entry(bd =5)
    entry.grid(row=9, column = 1, columnspan=5, sticky=W+E)
    bo = tk.Button(text="Original Page",command=web)
    bo.grid( row = 14, column = 5, columnspan=2, padx = 15, pady = 15)

    optionList = ('Restart (choose color from list)','red', 'green', 'blue', 'purple')
    global v
    v = StringVar()
    v.set(optionList[0])
    defaultOption = StringVar()
    om = OptionMenu(root, v, *optionList)
    defaultOption.set(DEFAULTVALUE_OPTION)
    om.grid(  row = 13, column = 0, columnspan=4, pady = 10)
    confirm = tk.Button(text="Confirm",command=restart)
    confirm.grid( row = 14, column = 1, columnspan=2)
    confirm.place(anchor= SE, x=160, y=320)
    
    root.mainloop()  

if __name__ == '__main__':
    main()  


