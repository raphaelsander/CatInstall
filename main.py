#!/usr/bin/env python
# -*- coding: UTF-8 -*-

## By Raphael Sander
## <raphael.sander75@gmail.com>

import gtk
import os
import sqlite3

from about import about

# Conectando ao banco de dados
conn = sqlite3.connect('data.db')

os.system("mkdir ~/.cacheappinstall/")

class AppInstall:

    def __init__(self):

        # Estrutura da janela principal
        self.window = gtk.Window()
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(400, 300)
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)
        self.window.set_title('AppInstall 0.1 (Beta)')
        self.window.set_border_width(15)

        # Caixa vertical
        self.VBox = gtk.VBox()

        # Caixa horizontais
        self.HBox1 = gtk.HBox()
        self.HBox2 = gtk.HBox()

        # Adicionando boxs horizontais ao box vertical
        self.VBox.pack_start(self.HBox1, expand=False, fill=True)
        self.VBox.pack_start(self.HBox2, expand=False, fill=True)

        # Adicionando box vertical na janela
        self.window.add(self.VBox)

        # Label Pesquisa
        self.search_label = gtk.Label("Pesquisar:  ")
        self.HBox1.pack_start(self.search_label, False, False, 0)

        # Entrada de pesquisa
        self.search = gtk.Entry()
        self.HBox1.pack_start(self.search, expand=True, fill=True)

        # Instalar
        self.install = gtk.Button("Instalar")
        self.install.connect('clicked', self.cmd_install)
        self.HBox2.pack_start(self.install, expand=False, fill=True)

        # About
        self.bot_about = gtk.Button("About")
        self.bot_about.connect('clicked', self.cmd_about)
        self.HBox2.pack_start(self.bot_about, expand=False, fill=True)

        self.window.show_all()

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def cmd_about(self, *args):
        about()

    def cmd_install(self, *args):
        print "Em desenvolvimento"
        #os.system("gnome-terminal -x bash -c /opt/AppInstall/apps/%s && exit; exec bash" % x)

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    AppInstall()
    main()