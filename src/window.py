import gi
import repo
import logs
from singleton import singleton

gi.require_version('Gtk', '3.0')

try:
    from gi.repository import Gtk
except ImportError:
    raise

glade_file = '../glade/vgit.glade'


class vgit_main(metaclass=singleton):
    def __init__(self):
        # create the builder
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        # load the widgets
        self.window = self.builder.get_object('vgit_main')
        self.logger = self.builder.get_object('vgit_msg')
        self.commit = self.builder.get_object('vgit_commits')
        self.ignore = self.builder.get_object('vgit_ignore_buffer')
        self.direct = self.builder.get_object('vgit_dir')

        # create the logger callback
        self.vgit_log_cb = lambda log:  self.logger.set_text(log)
        self.window.show()

        # create the log instance
        self.logs = logs.vgit_logger()
        # create the repo instance
        self.repo = repo.vgit_repo()

    def vgit_main_destroy_cb(self, object, data=None):
        Gtk.main_quit()

    def vgit_clone_button_click(self, button, data=None):
        url = self.builder.get_object('vgit_clone_url_entry').get_text()
        path = self.direct.get_current_folder()

        if path is None:
            self.logs.vgit_general_error("No path name to clone...",
                                         self.vgit_log_cb)
            return

        # log that the clone has started
        self.logs.vgit_clone_started(url, path, self.vgit_log_cb)

        # start the clone
        if self.repo.vgit_clone(path, url, self.vgit_log_cb):
            # log that the clone has ended
            self.logs.vgit_clone_finish(self.vgit_log_cb)

            # load the commits of the clonned repository
            self.vgit_dir_current_folder_changed(self)

    def vgit_init_button_click(self, object, data=None):
        path = self.builder.get_object('vgit_dir').get_current_folder()
        bare = self.builder.get_object('vgit_init_bare_toggle').get_active()

        if path is None:
            self.logs.vgit_general_error("No path name...", self.vgit_log_cb)
            return

        # create the repository
        if self.repo.vgit_init(path, self.vgit_log_cb, bare=bare):
            # log that a repository was created
            self.logs.vgit_init(path, self.vgit_log_cb)

    def vgit_dir_current_folder_changed(self, object, data=None):
        # TODO: load the contents of the git ignore into the ignore text buffer
        self.vgit_ignore_load()
        self.commit.get_buffer().set_text("")
        self.repo.vgit_load_repo(path=self.builder.get_object('vgit_dir')
                                 .get_current_folder())
        self.repo.vgit_commits(lambda log: self.commit.get_buffer()
                               .insert_at_cursor(log))

    def vgit_ignore_load(self):
        path_name = self.direct.get_current_folder()

        if path_name is None:
            self.builder.get_object('vgit_ignore_buffer')\
                        .get_buffer()\
                        .set_text("")
            return

        try:
            with open(path_name + '/.gitignore', "r") as file:
                text = ""
                for line in file:
                    text += (line)
                self.builder.get_object('vgit_ignore_buffer')\
                            .get_buffer()\
                            .set_text(text)

        except IOError:
            self.builder.get_object('vgit_ignore_buffer')\
                        .get_buffer()\
                        .set_text("")

            return

    def vgit_ignore_save_click(self, button, data=None):
        text_buffer = self.builder.get_object('vgit_ignore_buffer')\
                                  .get_buffer()
        text = text_buffer.get_text(text_buffer.get_start_iter(),
                                    text_buffer.get_end_iter(),
                                    False)

        path_name = self.direct.get_current_folder()
        if path_name is None:
            print("aaa")
            self.logs.vgit_general_error("No path name...", self.vgit_log_cb)
            return

        file_name = path_name + '/.gitignore'

        with open(file_name, "w") as file:
            file.write(text)

        self.logs.vgit_ignore_save(self.vgit_log_cb)

    def vgit_add_add_all_click(self, button, data=None):
        # TODO: add all modified files
        if self.repo.vgit_add_all(self.vgit_log_cb):
            self.log.vgit_add_all(self.vgit_log_cb)
