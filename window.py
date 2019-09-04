import gi
import repo
import logs

gi.require_version('Gtk', '3.0')

try:
    from gi.repository import Gtk
except ImportError:
    raise


class vgit_main:
    def __init__(self):
        # create the builder
        self.glade_file = 'glade/vgit.glade'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        # load the widgets
        self.window = self.builder.get_object('vgit_main')
        self.vgit_input = self.builder.get_object('vgit_input')
        self.vgit_log = self.builder.get_object('vgit_log')
        self.logger = logs.vgit_logger()

        def vgit_log_cb(log):
            self.vgit_log.get_buffer().insert_at_cursor(log)

        self.logger.vgit_load_logs(vgit_log_cb)

        self.window.show()

    def vgit_main_destroy_cb(self, object, data=None):
        self.logger.vgit_close_logs()
        Gtk.main_quit()

    def vgit_clone_start_clicked_cb(self, button, data=None):

        self.vgit_clone_url = self.builder.get_object('vgit_clone_url')
        self.vgit_dir = self.builder.get_object('vgit_dir')

        self.url = self.vgit_clone_url.get_text()
        self.path = self.vgit_dir.get_current_folder()

        if self.path is None:
            # TODO: log error here
            print('Err')
            return

        def vgit_log_cb(log):
            self.vgit_log.get_buffer().insert_at_cursor(log)

        self.logger.vgit_clone_started(self.url, self.path, vgit_log_cb)
        # TODO: add erro callback here
        repo.vgit_repo.vgit_clone(self.path, self.url)

        self.logger.vigt_clone_finish(vgit_log_cb)
