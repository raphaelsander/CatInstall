#!/usr/bin/python3.5
# coding=UTF-8

# By Team BlackCat

import os
import json
import requests
import urllib2
import hashlib

from PyQt4.QtGui import QApplication, QMainWindow
from ui import Ui

class App():

    def __init__(self):

        # Criando pasta de cache.
        if os.path.exists(os.path.expanduser("~/.cache/")):
            pass
        else:
            try:
                os.mkdir(os.path.expanduser("~/.cache/"))
            except OSError:
                print("Erro ao criar a pasta de cache. Verifique as permissões do software.")

        # Criando pasta onde serão salvos os scripts e dados do software.
        if os.path.exists(os.path.expanduser("~/.local/share/CatInstall/")):
            pass
        else:
            try:
                os.mkdir(os.path.expanduser("~/.local/share/CatInstall/"))
                os.mkdir(os.path.expanduser("~/.local/share/CatInstall/scripts/"))
            except OSError:
                print("Erro ao criar a pasta de dados do software. Verifique as permissões do software. :)")

        # Atualizando CHANGELOG
        url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/CHANGELOG")
        try:
            os.remove(os.path.expanduser("~/.local/share/CatInstall/CHANGELOG"))
        except OSError:
            print("Erro ao remover CHANGELOG, talvez o arquivo não exista. :)")

        try:
            with open(os.path.expanduser("~/.local/share/CatInstall/CHANGELOG"), 'wb') as output:
                output.write(url.read())
        except OSError:
            print("Erro ao criar arquivo CHANGELOG, verifique as permissões do software. :)")

        # Abrindo arquivo de CHANGELOG que irá efetuar o controle de versão dos scripts
        try:
            changelog = open(os.path.expanduser("~/.local/share/CatInstall/CHANGELOG"), 'r')
            data_changelog = json.load(changelog)
        except IOError:
            print("Arquivo de CHANGELOG não existe. É necessário internet!!!! :)")

        for category in data_changelog:

            # Criando pasta para cada categoria de script
            if os.path.exists(os.path.expanduser("~/.local/share/CatInstall/scripts/%s" % category)):
                pass
            else:
                try:
                    os.mkdir(os.path.expanduser("~/.local/share/CatInstall/scripts/%s" % category))
                except OSError:
                    print("Erro ao criar a pasta de script para %s. Verifique as permissões do software. :)" % category)

            # Carregando o arquivo de CHANGELOG e transformando os scripts em objetos
            for script in data_changelog['%s' % category]:
                name = data_changelog[category][script]['name']
                patch = os.path.expanduser("~/.local/share/CatInstall") + data_changelog[category][script]['patch']
                md5 = data_changelog[category][script]['md5']

                script = Script(name, category, patch, md5)

                script.update(name, category, patch, md5)

                script.add_row()

class Script(object):

    def __init__(self, name, category, patch, md5):
        self.name = name
        self.patch = patch
        self.md5 = md5
        self.category = category

        print self.name, self.category, self.patch, self.md5

    def add_row(self):
        pass
        #listbox = builder.get_object("listbox_%s" % category)
        #row = Gtk.ListBoxRow()
        #hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=80)
        #row.add(hbox)
        #row.show()
        #vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        #hbox.pack_start(vbox, True, True, 0)
        #label = Gtk.Label("%s" % name, xalign=0)
        #vbox.pack_start(label, True, True, 0)

        """button = Gtk.Button("Execute")
        button.connect('clicked', self.install, patch)
        hbox.pack_start(button, False, True, 0)
        listbox.add(row)

        vbox.show()
        hbox.show()
        row.show()
        button.show()
        label.show()"""

    def update(self, name, category, patch, md5):

        hash_md5 = hashlib.md5()

        # Verificando se o script existe localmente, caso não exista baixa diretamente do site
        if os.path.isfile(patch):
            pass
        else:
            try:
                url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/scripts/%s/%s" % (category, patch.split("/")[-1]))
                with open('%s' %patch, 'wb') as output:
                    output.write(url.read())
            except IOError:
                print("Não foi possível baixar e escrever o script. Reinicie o aplicativo com internet!!! :)")

        # Extraindo MD5 do script local
        try:
            with open(patch, "rb") as file:
                for ped in iter(lambda: file.read(4096), b""):
                    hash_md5.update(ped)
        except IOError:
            print("Não foi possível ler o script local. Reinicie o aplicativo com internet!!! :)")

        # Comparando o MD5 do CHANGELOG e do script local, caso diferente é feito o download novamente
        if hash_md5.hexdigest() == md5:
            pass
        else:
            try:
                os.remove("%s" % patch)
            except OSError:
                print("Não foi possível excluir o script desatualizado. Talvez ele tenha sumido. :/")
            try:
                url = urllib2.urlopen("http://catinstall.blackcat8080.xyz/scripts/%s/%s" % (category, patch.split("/")[-1]))
                with open('%s' %patch, 'wb') as output:
                    output.write(url.read())
            except IOError:
                print("Não foi possível baixar e escrever o script. Reinicie o aplicativo com internet!!! :)")

    def install(self, button, patch):
        try:
            os.system("chmod +x '%s'" %patch)
        except OSError:
            print("Não foi possível alterar as permissões do script. :/")
        try:
            os.system("gnome-terminal -x bash -c '%s' && exit; exec bash" %patch)
        except OSError:
            print("Não foi possível executar o script. Será que você possui o gnome-terminal? :/")

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui()
    main_window.setupUi(window)
    window.show()
    app.exec_()
    main = App()