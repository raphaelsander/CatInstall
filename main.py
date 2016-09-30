#!/usr/bin/python3
# coding=UTF-8

# By Team BlackCat

import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

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
		self.window2 = self.builder.get_object("window2")
		self.aboutdialog = self.builder.get_object("aboutdialog1")

		self.window1.set_name('window1')
		self.window2.set_name('window2')
		self.aboutdialog.set_name('aboutdialog1')

		home = ["apps", "themes", "icons", "fonts", "cursor", "conky", "other"]

		self.x = True

		for y in home:
			self.builder.get_object("%s" %y).connect('clicked', self.aplicativos, "%s" %y)

		style_provider = Gtk.CssProvider()

		css = "@import url('%s');" %(os.getcwd() + "/ui/style.css")

		style_provider.load_from_data(bytes(css.encode()))
		Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

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
		print ("Exibindo janela de %s" %categoria)
		self.window1.hide()

		self.btn = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
		self.btt = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

		for i in range(0, 9):
			self.window2 = self.builder.get_object("window2")
			self.btt[i] = self.builder.get_object("%s" %i)
			self.btt[i].set_label("%s" % apps[i])
			self.btn[i] = self.btt[i].connect('clicked', self.install_app, categoria, "%s" %apps[i])
			print(self.btn[i], self.btt[i])

		try:
			self.builder.get_object("home").disconnect(yuuu)
		except:
			yuuu = self.builder.get_object("home").connect('clicked', self.home, self.btn, self.btt)
		self.window2.show_all()

	def next(self, data=None):
		print ("Próxima página")

	def back(self, data=None):
		print("Página anterior")

	def home(self, button, arg, btt, *args):
		print ("Voltando ao Início")
		print(arg)
		print(btt)
		for i in range(0, 8):
			self.btt[i].disconnect(arg[i])
		self.window2.hide()
		self.window1.show()

	def install_app(self, null, categoria, name_app):
		scripts_path = os.getcwd() + "/%s/" %categoria
		print ("Executando Script", (scripts_path + name_app))
		os.system("chmod +x '%s%s'" %(scripts_path, name_app))
		os.system("gnome-terminal -x bash -c '%s%s' && exit; exec bash" %(scripts_path, name_app))

if __name__ == '__main__':
    app = App()
    Gtk.main()
