from tkinter import *
import os

def openRpg():
	os.system("python RpgText.py")
	app.destroy()
	os.system("python interface.py")


def openHand():
	os.system("python visaoComp.py")
	#break

app = Tk()

class Main_app():
	rpgbt = Button(app,text="Jogar Stone land (Rpg texto)",command=openRpg).pack()
	vscbt = Button(app, text="Testar Reconhecimento de mãos",command=openHand).pack()


app.geometry("200x200")
app.mainloop()
