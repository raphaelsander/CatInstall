#!/usr/bin/python3
#coding=UTF-8

## By Raphael Sander
## <raphael.sander75@gmail.com>

from Tkinter import *
from PIL import ImageTk, Image
import os
import os.path

os.system("mkdir ~/.cacheappinstall/")

class App:
	def __init__(self, master):
		
		self.img=[0,1,2,3,4,5,6,7,8,9,10,11,12]
		self.var=[0,1,2,3,4,5,6,7,8,9,10,11,12]
		
		frame = Frame(master)
		frame.grid()
		for x in range(0,12):
			self.var[x] = IntVar()
		
		Button(relief=FLAT, command = self.bash, text="Instalar").grid(column=1, row=6)
		Button(relief=FLAT, command = self.bash, text="About").grid(column=3, row=6)
		
		for x in range(0,12):
			self.img[x]=ImageTk.PhotoImage(Image.open(u"/opt/AppInstall/images/noinstalled/%s.png" %x))
			if x<6:
				Label(image=self.img[x]).grid(column=1, row=x)
				Checkbutton(master, variable=self.var[x]).grid(column=0, row=x)
			else:
				Label(image=self.img[x]).grid(column=3, row=x-6)
				Checkbutton(master, variable=self.var[x]).grid(column=2, row=x-6)
		
	def bash(self):
		for x in range(0,12):
			if self.var[x].get()==1:
				os.system("gnome-terminal -x bash -c /opt/AppInstall/apps/%s && exit; exec bash" %x)
			
def main():
	
	root = Tk()
	app = App(root)
	root.title('AppInstall')
	root.geometry('500x360+100+250')
	root.maxsize(500, 360)
	icon = ImageTk.PhotoImage(Image.open(u"/opt/AppInstall/icon.png"))
	root.tk.call('wm', 'iconphoto', root._w, icon)
	root.mainloop()
	
if __name__ == '__main__':
	main()
