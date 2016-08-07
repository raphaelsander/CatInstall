#!/usr/bin/python3
# coding=UTF-8

# By Raphael Sander
# <raphael.sander75@gmail.com>

import os
import os.path
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if os.path.exists(os.getcwd() + "/.cacheappinstall/") == True:
    pass
else:
    os.system("mkdir %s/.cacheappinstall/" os.getcwd())

class App(Gtk.Window):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file(os.getcwd() + "/AppInstall/main.glade")
        window = builder.get_object("window1")
        window.set_title("AppInstall 1.0 Beta")

        builder.connect_signals({
            "about": self.sobre()
        })

        window.show()
        window.connect("delete-event", Gtk.main_quit)

    def sobre(self):
        builder = Gtk.Builder()
        builder.add_from_file(os.getcwd() + "/AppInstall/main.glade")
        window = builder.get_object("aboutdialog1")
        window.set_title("Sobre")

    #     self.aboutw = None
    #     self.img = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #     self.var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #
    #     frame = Frame(master)
    #     frame.grid()
    #     for x in range(0, 12):
    #         self.var[x] = IntVar()
    #
    #     Button(relief=FLAT, command=self.bash, text="Instalar").grid(column=1, row=6)
    #     Button(relief=FLAT, command=self.about, text="About").grid(column=3, row=6)
    #
    #     for x in range(0, 12):
    #         self.img[x] = ImageTk.PhotoImage(Image.open(u"%s/images/noinstalled/%s.png" % (p, x)))
    #         if x < 6:
    #             Label(image=self.img[x]).grid(column=1, row=x)
    #             Checkbutton(master, variable=self.var[x]).grid(column=0, row=x)
    #         else:
    #             Label(image=self.img[x]).grid(column=3, row=x - 6)
    #             Checkbutton(master, variable=self.var[x]).grid(column=2, row=x - 6)
    #
    # def bash(self):
    #     for x in range(0, 12):
    #         if self.var[x].get() == 1:
    #             os.system("gnome-terminal -x bash -c %s/apps/%s && exit; exec bash" % (p, x))
    #
    # def about(self):
    #     if self.aboutw is None:
    #         self.aboutw = Tk()
    #         self.aboutw.title('Sobre')
    #         self.aboutw.geometry('500x360+100+250')
    #         self.aboutw.maxsize(500, 360)
    #         self.aboutw.protocol("WM_DELETE_WINDOW", self.close_about)
    #         self.icon = ImageTk.PhotoImage(Image.open(u"%s/icon.png" % p))
    #
    #     else:
    #         self.aboutw.lift()
    #
    # def close_about(self):
    #     self.aboutw.destroy()
    #     self.aboutw = None

if __name__ == '__main__':
    app = App()
    Gtk.main()