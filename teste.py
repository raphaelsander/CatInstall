import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class _UiProxy(object):

    def __init__(self):
        self._builder = Gtk.Builder()
        gladefile = os.getcwd() + "/main.glade"
        self._builder.add_from_file(gladefile)
        self.about_window = self._builder.get_object("about_window")

    def __getattr__(self, attr):
        return self._builder.get_object(attr)


class CatApp(object):

    def __init__(self):
        self._ui = _UiProxy()
        self._setup()

    #
    #  Public
    #

    #
    #  Private
    #

    def _install_app(self, app):
        scripts_path = os.getcwd() + "/apps/"
        os.system("gnome-terminal -x bash -c %s%s && exit; exec bash" %
                  (scripts_path, app))

    def _setup(self):
        # Main window
        main_window = self._ui.main_window
        main_window.connect("destroy", Gtk.main_quit)

        self._ui.chrome_btn.connect('clicked', self._on_chrome_btn__clicked)
        self._ui.everpad_btn.connect('clicked', self._on_everpad_btn__clicked)
        self._ui.numix_btn.connect('clicked', self._on_numix_btn__clicked)
        self._ui.popcorn_btn.connect('clicked', self._on_popcorn_btn__clicked)
        self._ui.recorder_btn.connect('clicked', self._on_recorder_btn__clicked)
        self._ui.skype_btn.connect('clicked', self._on_skype_btn__clicked)
        self._ui.spotify_btn.connect('clicked', self._on_spotify_btn__clicked)
        self._ui.steam_btn.connect('clicked', self._on_steam_btn__clicked)
        self._ui.studio_btn.connect('clicked', self._on_studio_btn__clicked)
        self._ui.subterfuge_btn.connect('clicked', self._on_subterfuge_btn__clicked)
        self._ui.telegram_btn.connect('clicked', self._on_telegram_btn__clicked)
        self._ui.ubuntu_tweak_btn.connect('clicked', self._on_ubuntu_tweak_btn__clicked)

        main_window.show_all()

        # About window
        about_window = self._ui.about_window
        self._ui.about_btn.connect('clicked', self._on_about_btn__clicked)

    def _show_about(self):
        self._ui.about_window.show_all()

    #
    #   Callbacks
    #

    # Aqui deve-se colocar os callbacks de todos os botoes que irao ocorrer a
    # instalacao

    def _on_about_btn__clicked(self, button):
        print "about"

    def _on_chrome_btn__clicked(self, button):
        print "chrome"
        self._install_app('chrome')

    def _on_everpad_btn__clicked(self, button):
        print "everpad"
        self._install_app('everpad')

    def _on_numix_btn__clicked(self, button):
        print "numix"
        self._install_app('numix')

    def _on_popcorn_btn__clicked(self, button):
        print "popcorn"
        self._install_app('popcorn')

    def _on_recorder_btn__clicked(self, button):
        print "recorder"
        self._install_app('recorder')

    def _on_skype_btn__clicked(self, button):
        print "skype"
        self._install_app('skype')

    def _on_spotify_btn__clicked(self, button):
        print "spotify"
        self._install_app('spotify')

    def _on_steam_btn__clicked(self, button):
        print "steam"
        self._install_app('steam')

    def _on_studio_btn__clicked(self, button):
        print "studio"
        self._install_app('android_studio')

    def _on_subterfuge_btn__clicked(self, button):
        print "subterfuge"
        self._install_app('subterfuge')

    def _on_telegram_btn__clicked(self, button):
        print "telegram"
        self._install_app('telegram')

    def _on_ubuntu_tweak_btn__clicked(self, button):
        print "tweak"
        self._install_app('ubuntu_tweak')


if __name__=='__main__':
    try:
        app = CatApp()
        Gtk.main()
    except KeyboardInterrupt:
        Gtk.main_quit
