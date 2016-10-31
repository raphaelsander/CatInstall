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
        self.window_home = self.builder.get_object("window_home")
        #self.window2 = self.builder.get_object("window2")
        self.aboutdialog = self.builder.get_object("aboutdialog1")

        self.window_home.set_name('window_home')
        #self.window2.set_name('window2')
        self.aboutdialog.set_name('aboutdialog1')

        home = ["app", "theme", "icon", "font", "cursor", "conky", "other"]

        for category in home:
            self.builder.get_object("button_%s" %category).connect('clicked', self.aplicativos, category)

        style_provider = Gtk.CssProvider()

        css = "@import url('%s');" % (os.getcwd() + "/ui/style.css")

        style_provider.load_from_data(bytes(css.encode()))
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        self.window_home.show()

    def about(self, data=None):
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()

    def window_home_destroy(self, data=None):
        Gtk.main_quit()

    def aplicativos(self, null, category):
        apps = os.listdir(os.getcwd() + "/scripts/%s/" %category)
        self.window_home.hide()

        self.window2 = self.builder.get_object("window_%s" %category)
        listbox = self.builder.get_object("listbox_%s" %category)

        for i in apps:

            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=80)
            row.add(hbox)
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            hbox.pack_start(vbox, True, True, 0)

            label = Gtk.Label("%s" %i, xalign=0)
            vbox.pack_start(label, True, True, 0)

            button = Gtk.Button("Execute")
            button.connect('clicked', self.install_app, category, '%s' %i)
            hbox.pack_start(button, False, True, 0)

            listbox.add(row)

        self.window2.show_all()

    def home(self, button):
        self.window2.hide()
        self.window_home.show()

    def install_app(self, null, category, name_app):
        scripts_path = os.getcwd() + "/scripts/%s/" %category
        os.system("chmod +x '%s%s'" %(scripts_path, name_app))
        os.system("gnome-terminal -x bash -c '%s%s' && exit; exec bash" %(scripts_path, name_app))


if __name__ == '__main__':
    app = App()
    Gtk.main()
