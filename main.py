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

    # This dictionary is a referente to script app using button label
    applications = {
        'Android Studio' : 'android_studio',
        'Chrome' : 'chrome',
        'Numix' : 'numix',
        'Popcorn Time' : 'popcorn',
        'SS Recorder' : 'simplescreenrecorder',
        'Skype' : 'skype',
        'Spotify' : 'spotify',
        'Steam' : 'steam',
        'Subterfuge' : 'subterfuge',
        'Telegram' : 'telegram',
        'Ubuntu Tweak' : 'ubuntu_tweak',
    }

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

        self._ui.chrome_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.numix_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.popcorn_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.recorder_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.skype_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.spotify_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.steam_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.studio_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.subterfuge_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.telegram_btn.connect('clicked', self._on_app_btn__clicked)
        self._ui.ubuntu_tweak_btn.connect('clicked', self._on_app_btn__clicked)

        main_window.show_all()

        # About window
        about_window = self._ui.about_window
        self._ui.about_btn.connect('clicked', self._on_about_btn__clicked)

    def _show_about(self):
        self._ui.about_window.show_all()

    #
    #   Callbacks
    #

    def _on_about_btn__clicked(self, button):
        print "about"

    def _on_app_btn__clicked(self, button):
        app_name = self.applications.get(button.get_label())
        self._install_app(app_name)


if __name__=='__main__':
    try:
        app = CatApp()
        Gtk.main()
    except KeyboardInterrupt:
        Gtk.main_quit
