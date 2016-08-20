#!/usr/bin/python3
# coding=UTF-8

# By Team BlackCat

import os
import os.path
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
		print "Exibindo Sobre"
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()

	def window1_destroy(self, data=None):
		print "Fechando"
		Gtk.main_quit()

	def aplicativos(self, data=None):
		aplicativos = os.listdir(os.getcwd() + "/apps/")
		print "Exibindo janela de Aplicativos"
		self.window.hide()
		self.window = self.builder.get_object("window2")
		for i in range(0, len(aplicativos)):
			print i, aplicativos[i]

			##Ainda em Construção
			self.button = Gtk.Button()
			self.grid5.attach(self.button, 0, i, 1, 1)

		self.window.show()

	def home(self, data=None):
		print "Voltando ao Início"
		self.window.hide()
		self.window = self.builder.get_object("window1")
		self.window.show()

	#def install_app(self, app):
		#scripts_path = os.getcwd() + "/apps/"
		#os.system("gnome-terminal -x bash -c %s%s && exit; exec bash" % (scripts_path, app))

	#def setup(self):
		#for i in self.applications:
			#button_name = "%s_btn" % i
			#getattr(self.main, button_name).connect('clicked', self._on_app_btn__clicked, i)

if __name__ == '__main__':
    app = App()
    Gtk.main()
