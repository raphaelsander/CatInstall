#!/usr/bin/python3.5
# coding=UTF-8

# By Team BlackCat

import os
import gi
import json
import requests
import urllib2
import hashlib
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class App:

    def __init__(self):
        # Criando pasta de Cache onde será salvo os downloads dos scripts
        if os.path.exists(os.getcwd() + "/.cache/"):
            pass
        else:
            try:
                os.mkdir(os.getcwd() + "/.cache/")
            except:
                print("Erro ao criar a pasta de cache. Verifique as permissões do software.")

        # Atualizando CHANGELOG
        url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/CHANGELOG")
        os.remove("CHANGELOG")
        with open('CHANGELOG', 'wb') as output:
            output.write(url.read())

        # Abrindo arquivo de CHANGELOG que irá efetuar o controle de versão dos scripts
        try:
            changelog = open('CHANGELOG', 'r')
            data_changelog = json.load(changelog)
        except:
            print("ERROR 05")

        # Construindo as janelas do app via XML Glade
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.getcwd() + "/ui/main.glade")
        self.window = self.builder.get_object("window")
        self.about_dialog = self.builder.get_object("about_dialog")
        self.builder.connect_signals(self)

        # Carregando o arquivo de CHANGELOG e transformando os scripts em objetos
        for category in data_changelog:
            for script in data_changelog['%s' % category]:
                name = data_changelog[category][script]['name']
                patch = os.getcwd() + data_changelog[category][script]['patch']
                md5 = data_changelog[category][script]['md5']

                script = Script(name, category, patch, md5)

                script.update(name, category, patch, md5)

                script.add_row(name, category, patch, self.builder)

        # Definindo nome para as janelas para aplicar estilo através do CSS
        self.window.set_name('window')
        self.about_dialog.set_name('window_about')

        style_provider = Gtk.CssProvider()
        css = "@import url('%s');" % (os.getcwd() + "/ui/style.css")
        style_provider.load_from_data(bytes(css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # Exibindo interface gráfica
        self.window.show_all()

    def on_button_about_clicked(self, data=None):
        self.response = self.about_dialog.run()
        self.about_dialog.hide()

    def window_destroy(self, data=None):
        Gtk.main_quit()

class Script(object):

    def __init__(self, name, category, patch, md5):
        self.name = name
        self.patch = patch
        self.md5 = md5
        self.category = category

        print self.name, self.category, self.patch, self.md5

    def add_row(self, name, category, patch, builder):
        listbox = builder.get_object("listbox_%s" % category)
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=80)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)
        label = Gtk.Label("%s" % name, xalign=0)
        vbox.pack_start(label, True, True, 0)

        button = Gtk.Button("Execute")
        button.connect('clicked', self.install, patch)
        hbox.pack_start(button, False, True, 0)
        listbox.add(row)

    def update(self, name, category, patch, md5):

        hash_md5 = hashlib.md5()

        # Verificando se o script existe localmente, caso não exista baixa diretamento do site
        if os.path.isfile(patch):
            pass
        else:
            try:
                url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/scripts/%s/%s" % (category, patch.split("/")[-1]))
                with open('%s' %patch, 'wb') as output:
                    output.write(url.read())
            except IOError:
                print("Error 04")

        # Extraindo MD5 do script local
        try:
            with open(patch, "rb") as file:
                for ped in iter(lambda: file.read(4096), b""):
                    hash_md5.update(ped)
        except IOError:
            print("Error 03")

        # Comparando o MD5 do CHANGELOG e do script local, caso diferente é feito o download novamente
        if hash_md5.hexdigest() == md5:
            pass
        else:
            try:
                url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/scripts/%s/%s" % (category, patch.split("/")[-1]))
                os.remove("%s" %patch)
                with open('%s' %patch, 'wb') as output:
                    output.write(url.read())
            except IOError:
                print("Error 00")

    def install(self, button, patch):
        try:
            os.system("chmod +x '%s'" %patch)
        except IOError:
            print("Error 01")
        try:
            os.system("gnome-terminal -x bash -c '%s' && exit; exec bash" %patch)
        except IOError:
            print("Error 02")

if __name__ == '__main__':
    app = App()
    Gtk.main()
