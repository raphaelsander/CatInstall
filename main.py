#!/usr/bin/python3
# coding=UTF-8

# By Team BlackCat

import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class App:

    def __init__(self):
        #Criação da pasta de cache
        if os.path.exists(os.getcwd() + "/.cacheappinstall/"):
            pass
        else:
            try:
                os.mkdir(os.getcwd() + "/.cacheappinstall/")
            except:
                print("Erro ao criar a pasta de cache. Verifique as permissões do software.")

        #Construindo toda a estrutura gráfica
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.getcwd() + "/ui/main.glade")
        self.window = self.builder.get_object("window")
        self.about_dialog = self.builder.get_object("about_dialog")
        self.builder.connect_signals(self)
        self.categories = ["app", "theme", "icon", "font", "cursor", "conky", "other"]

        cont = 0

        for self.category in self.categories:
            print("------------%s------------" %self.category)
            listbox = self.builder.get_object("listbox_%s" %self.category)
            for i in os.listdir(os.getcwd() + "/scripts/%s/" % self.category):
                row = Gtk.ListBoxRow()
                hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=80)
                row.add(hbox)
                vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
                hbox.pack_start(vbox, True, True, 0)
                label = Gtk.Label("%s" %i, xalign=0)
                vbox.pack_start(label, True, True, 0)

                button = Gtk.Button("Execute")
                patch = os.getcwd() + "/scripts/%s/%s" %(self.category, i)
                print(patch)
                button.connect('clicked', self.install_app, patch)
                hbox.pack_start(button, False, True, 0)
                listbox.add(row)

                cont = cont + 1

        #Definindo estilo CSS
        self.window.set_name('window')
        self.about_dialog.set_name('window_about')

        style_provider = Gtk.CssProvider()
        css = "@import url('%s');" % (os.getcwd() + "/ui/style.css")
        style_provider.load_from_data(bytes(css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        print("Total de %s scripts, ajude a aumentar esse número! Acesse http://blackcat8080.xyz/catinstall" %cont)
        self.window.show_all()

    #Função responsável por exibir a janela sobre
    def on_button_about_clicked(self, data=None):
        self.response = self.about_dialog.run()
        self.about_dialog.hide()

    #Função responsável por matar o programa após fechar a janela
    def window_destroy(self, data=None):
        Gtk.main_quit()

    #Função responsável por executar os scripts
    def install_app(self, widget, patch):
        try:
            os.system("chmod +x '%s'" % patch)
        except:
            print("Erro ao trocar a permissão do script. Verifique as permissões.")
        try:
            os.system("gnome-terminal -x bash -c '%s' && exit; exec bash" % patch)
        except:
            print("Erro ao executar o script. Verifique as permissões e o código do mesmo.")

if __name__ == '__main__':
    app = App()
    Gtk.main()
