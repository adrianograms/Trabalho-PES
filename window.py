import gi
gi.require_version('Gtk', '3.0')

try:
    from gi.repository import Gtk
except ImportError:
    raise


class vgit_main:
    def __init__(self):
        self.glade_file = 'glade/vgit.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('vgit_main')
        self.window.show()

    def vgit_main_destroy_cb(self, object, data=None):
        # move to a event log handler
        print("Closing")
        Gtk.main_quit()
