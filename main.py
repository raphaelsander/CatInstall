#!/usr/bin/python3
# coding=UTF-8

# By Team BlackCat

import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if os.path.exists(os.getcwd() + "/.cacheappinstall/") == True:
    pass
else:
    os.mkdir(os.getcwd() + "/.cacheappinstall/")

class App():

	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(os.getcwd() + "/ui/main.glade")
		self.builder.connect_signals(self)
		self.window1 = self.builder.get_object("window1")
		self.aboutdialog = self.builder.get_object("aboutdialog1")

		home = ["apps", "themes", "icons", "fonts", "cursor", "conky", "other"]

		for y in home:
			print(y)
			self.builder.get_object("%s" % y).connect('clicked', self.aplicativos, "%s" % y)

		self.window1.show()

	def about(self, data=None):
		print ("Exibindo Sobre")
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()

	def window1_destroy(self, data=None):
		print ("Fechando")
		Gtk.main_quit()

	def aplicativos(self, null, categoria):
		apps = os.listdir(os.getcwd() + "/%s/" %categoria)
		print ("Exibindo janela de Aplicativos")
		self.window1.hide()

		try:
			self.window2.show_all()
		except:
			self.window2 = self.builder.get_object("window2")
			for i in range(0, 9):
				self.builder.get_object("%s" %i).set_label("%s" %apps[i])
				self.builder.get_object("%s" %i).connect('clicked', self.install_app, categoria,"%s" %apps[i])
			self.window2.show_all()

	def next(self, data=None):
		print ("Próxima página")

	def back(self, data=None):
		print("Página anterior")

	def home(self, data=None):
		print ("Voltando ao Início")
		self.window2.hide()
		self.window1 = self.builder.get_object("window1")
		self.window1.show()

	def install_app(self, null, categoria, name_app):
		scripts_path = os.getcwd() + "/%s/" %categoria
		print ("Executando Script", (scripts_path + name_app))
		os.system("chmod +x '%s%s'" %(scripts_path, name_app))
		os.system("gnome-terminal -x bash -c '%s%s' && exit; exec bash" %(scripts_path, name_app))

if __name__ == '__main__':
    app = App()
    Gtk.main()
