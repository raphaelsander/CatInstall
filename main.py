#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## By Raphael Sander
## <raphael.sander75@gmail.com>

import gtk
import os
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('data.db')

os.system("mkdir ~/.cacheappinstall/")


class AppInstall:

    def destroy(self, widget):
        gtk.main_quit()

    def aboutdialog(self, widget):
        self.builder = gtk.Builder()
        self.builder.add_from_file("mainwindow.glade")
        self.builder.connect_signals('on_mainwindow_destroy', self.destroy)
        self.windowabout = self.builder.get_object("aboutdialog")
        self.windowabout.show()

    def __init__(self):
        # Estrutura da janela principal
        self.builder = gtk.Builder()
        self.builder.add_from_file("mainwindow.glade")
        self.builder.connect_signals({"on_mainwindow_destroy": self.destroy, \
                                      "on_janitor_button_toggled": gtk.main_quit, \
                                      "on_admins_button_toggled": gtk.main_quit, \
                                      "on_admins_button_clicked": gtk.main_quit, \
                                      "on_tweaks_button_toggled": gtk.main_quit, \
                                      "on_tweaks_button_clicked": gtk.main_quit, \
                                      "on_apps_button_toggled": gtk.main_quit, \
                                      "on_overview_button_toggled": gtk.main_quit, \
                                      "on_preference_button_clicked": gtk.main_quit, \
                                      "on_about_button_clicked": self.aboutdialog})
        self.window = self.builder.get_object("mainwindow")
        self.window.show()


if __name__ == "__main__":
    AppInstall()
    gtk.main()
