#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

def about():

    # Estrutura da janela principal
    window = gtk.Window()
    window.set_position(gtk.WIN_POS_CENTER)
    window.connect("destroy", destroy)
    window.set_title('About AppInstall')
    window.set_border_width(15)

    # Caixa vertical
    VBox = gtk.VBox()
    window.add(VBox)

    # Criando Box horizontal
    HBox1 = gtk.HBox()
    VBox.pack_start(HBox1, expand=True, fill=True)

    HBox2 = gtk.HBox()
    VBox.pack_start(HBox2, expand=True, fill=True)

    HBox3 = gtk.HBox()
    VBox.pack_start(HBox3, expand=True, fill=True)

    # Componentes
    text_about_title = gtk.Label("Sobre o AppInstall")
    HBox1.pack_start(text_about_title, expand=False, fill=True)

    img_about = gtk.Image()
    img_about.set_from_file("about.png")
    img_about.show()
    HBox2.pack_start(img_about, expand=False, fill=True)

    text_about = gtk.Label()
    text_about.set_markup("<big>Versão 0.3 (Beta)</big>, ""<b>bold</b>, <i>italic</i> and even point to ""somewhere in the <a href=\"http://www.black-cat.esy.es/appinstall/appinstall\" ""title=\"Click to find out more\">internets</a>.")
    text_about.set_line_wrap(True)
    HBox3.pack_start(text_about, expand=False, fill=True)

    window.show_all()
    gtk.main()

def destroy(*args):
    gtk.main_quit()