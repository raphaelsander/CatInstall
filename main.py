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

        for y in home:
            self.builder.get_object("%s" % y).connect('clicked', self.aplicativos, '%s' %y)

        style_provider = Gtk.CssProvider()

        css = "@import url('%s');" % (os.getcwd() + "/ui/style.css")

        style_provider.load_from_data(bytes(css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.window1.show()

    def about(self, data=None):
        print("Exibindo Sobre")
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def window1_destroy(self, data=None):
        print("Fechando")
        Gtk.main_quit()

    def aplicativos(self, button, categoria):
        apps = os.listdir(os.getcwd() + "/%s/" % categoria)
        print("Exibindo janela de %s" % categoria)
        self.window1.hide()
        self.window2 = self.builder.get_object("window2")

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        for i in apps:
            print(i)

            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            hbox.pack_start(vbox, True, True, 0)

            label = Gtk.Label("%s" %i, xalign=0)
            vbox.pack_start(label, True, True, 0)

            button = Gtk.Button("Execute")
            hbox.pack_start(button, False, True, 0)

            listbox.add(row)

        scroll = self.builder.get_object("scrolledwindow1")
        scroll.add_with_viewport(listbox)

        self.window2.show_all()

    def next(self, data=None):
        pass

    def back(self, data=None):
        pass

    def home(self, button):
        print("Voltando ao Início")
        self.window2.hide()
        self.window1.show()

    def install_app(self, null, categoria, name_app):
        scripts_path = os.getcwd() + "/%s/" % categoria
        print("Executando Script", (scripts_path + name_app))
        os.system("chmod +x '%s%s'" % (scripts_path, name_app))
        os.system("gnome-terminal -x bash -c '%s%s' && exit; exec bash" % (scripts_path, name_app))


if __name__ == '__main__':
    app = App()
    Gtk.main()
