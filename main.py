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
		self.builder.add_from_file(os.getcwd() + "/main.glade")
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window1")
		self.aboutdialog = self.builder.get_object("aboutdialog1")
		self.window.show()
		
	def on_about_activate(self, data=None):
		print "Exibindo Sobre"
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()
		
	def on_window1_destroy(self, data=None):
		print "Fechando"
		Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()
