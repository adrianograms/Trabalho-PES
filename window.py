import gi
import repo

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
        self.vgit_input = self.builder.get_object('vgit_input')
        self.vgit_log = self.builder.get_object('vgit_log')
        self.window.show()

    def vgit_main_destroy_cb(self, object, data=None):
        Gtk.main_quit()

    def vgit_clone_start_clicked_cb(self, button, data=None):

        self.vgit_clone_url = self.builder.get_object('vgit_clone_url')
        self.vgit_dir = self.builder.get_object('vgit_dir')

        self.url = self.vgit_clone_url.get_text()
        self.path = self.vgit_dir.get_current_folder()

        if self.path is None:
            # TODO: log error here
            return
        # TODO: move this to vgit_log
        print('clonning from -> ' + self.url + ' ' +
              'to -> ' + self.path)

        repo.vgit_repo.vgit_clone(self.path, self.url)
