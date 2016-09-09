#!/usr/bin/python3
# coding=UTF-8

# By Team BlackCat

import os
#import os.path
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if os.path.exists(os.getcwd() + "/.cacheappinstall/") == True:
    pass
else:
    os.mkdir(os.getcwd() + "/.cacheappinstall/")

class App(Gtk.Window):

	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(os.getcwd() + "/ui/main.glade")
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window1")
		self.aboutdialog = self.builder.get_object("aboutdialog1")
		self.window.show()
		
	def about(self, data=None):
		print ("Exibindo Sobre")
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()

	def window1_destroy(self, data=None):
		print ("Fechando")
		Gtk.main_quit()

	def aplicativos(self, apps, *args):
		apps = os.listdir(os.getcwd() + "/apps/")
		print ("Exibindo janela de Aplicativos")
		self.window.hide()
		self.window = self.builder.get_object("window2")

		#img = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

		#for i in range(0, len(apps)):
		for i in range(0, 9):
			img = Gtk.Image()
			img.set_from_file(os.getcwd() + "/ui/apps/%s.svg" %apps[i])
			#print(i, apps[i], img[i])
			#app = ("%s" % apps[i])
			self.builder.get_object("%s" %i).set_label("%s" %apps[i])
			self.builder.get_object("%s" %i).connect('clicked', self.install_app, apps[i])
			self.builder.get_object("%s" %i).set_image(img)
		self.window.show_all()

	def home(self, data=None):
		print ("Voltando ao Início")
		self.window.hide()
		self.window = self.builder.get_object("window1")
		self.window.show()

	def install_app(self, apps, *args):
		scripts_path = os.getcwd() + "/apps/"
		print (scripts_path)
		os.system("gnome-terminal -x bash -c %s%s && exit; exec bash" %(scripts_path, apps))
		print (scripts_path, app)

	#def setup(self):
		#for i in self.applications:
			#button_name = "%s_btn" % i
			#getattr(self.main, button_name).connect('clicked', self._on_app_btn__clicked, i)

if __name__ == '__main__':
    app = App()
    Gtk.main()
