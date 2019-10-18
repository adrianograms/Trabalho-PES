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
        # create the call back
        self.vgit_log_cb = lambda log: self.vgit_log.get_buffer().insert_at_cursor(log)
        self.window.show()
        # start the logs
        self.logger = logs.vgit_logger()
        self.logger.vgit_load_logs(self.vgit_log_cb)
        # create the call back

    def vgit_main_destroy_cb(self, object, data=None):
        """call back for when closing the main vgit window"""
        self.logger.vgit_close_logs()
        Gtk.main_quit()

    def vgit_clone_start_clicked_cb(self, button, data=None):
        """call back to star clone"""
        vgit_clone_url = self.builder.get_object('vgit_clone_url')
        vgit_dir = self.builder.get_object('vgit_dir')

        url = vgit_clone_url.get_text()
        path = vgit_dir.get_current_folder()

        if path is None:
            self.logger.vgit_general_error("no path name selected\n", self.vgit_log_cb)
            return

        # log that the clone has started
        self.logger.vgit_clone_started(url, path, self.vgit_log_cb)

        repo.vgit_repo.vgit_clone(path, url)
        # log that the clone has ended
        self.logger.vigt_clone_finish(self.vgit_log_cb)

    def vgit_init_start_clicked_cb(self, object, data=None):
        vgit_dir = self.builder.get_object('vgit_dir')
        vgit_init_bare = self.builder.get_object('vgit_init_bare')
        vgit_init_switch = self.builder.get_object('vgit_init_bare')

        path = vgit_dir.get_current_folder()

        if path is None:
            self.logger.vgit_general_error("no path name selected\n", self.vgit_log_cb)
            return

        if vgit_init_switch.get_state():
            print('bare')
        else:
            print('normal')

        repo.vgit_repo.vgit_init(path, bool(vgit_init_switch.get_state()))
        self.logger.vgit_init(path, self.vgit_log_cb)
