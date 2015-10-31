#!/usr/bin/env python
# coding=UTF-8

## By Raphael Sander
## <raphael.sander75@gmail.com>

import gtk
import os
import sqlite3

from about import about

os.system("mkdir ~/.cacheappinstall/")

class AppInstall:
    def __init__(self):

        # Estrutura da janela principal
        self.window = gtk.Window()
        self.window.set_title('AppInstall 0.1 (Beta)')
        self.window.set_border_width(15)

        # Caixa vertical
        self.VBox = gtk.VBox()

        # Caixa horizontal de pesquisa
        self.searchbox = gtk.HBox()

        # Criando itens e adicionando ao box de pesquisa
        self.search_label = gtk.Label("Pesquisar:  ")
        self.searchbox.pack_start(self.search_label, False, False, 0)

        self.search = gtk.Entry()
        self.searchbox.pack_start(self.search, expand=True, fill=True)

        # Box inferior
        self.footh = gtk.HBox()

        # Criando botões de instalação e about
        self.install = gtk.Button("Instalar")
        self.install.connect('clicked', self.cmd_install)
        self.footh.pack_start(self.install, expand=False, fill=True)

        self.bot_about = gtk.Button("About")
        self.bot_about.connect('clicked', self.cmd_about)
        self.footh.pack_start(self.bot_about, expand=False, fill=True)

        # Adicionando boxs horizontais ao box vertical
        self.VBox.pack_start(self.searchbox, expand=False, fill=True)
        self.VBox.pack_start(self.footh, expand=False, fill=True)

        # Adicionando box vertical na janela e exibindo
        self.window.add(self.VBox)

    def cmd_about(self, *args):
        about()

    def show(self):
        self.window.show_all()

    def cmd_install(self, *args):
        print "Em desenvolvimento"
        #os.system("gnome-terminal -x bash -c /opt/AppInstall/apps/%s && exit; exec bash" % x)

app = AppInstall()

if __name__ == "__main__":
    app.show()
    gtk.main()
