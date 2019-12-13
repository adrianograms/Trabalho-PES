import time
from singleton import singleton


class vgit_logger(metaclass=singleton):

    def format_with_time(self, string):
        return time.strftime("[%Y-%m-%d %H:%M:%S]",
                             time.localtime()) + ' ' + string

    def vgit_clone_started(self, url, path, vgit_log_cb):
        """Log when clone has started"""
        vgit_log_cb(self.format_with_time('Clonning from -> '
                                          + url + ' ' + 'to -> ' + path))

    def vgit_clone_finish(self, vgit_log_cb):
        """Long when clone has finished """
        vgit_log_cb(self.format_with_time('Clone finished.'))

    def vgit_general_error(self, what, vgit_log_cb):
        """Log a general error log"""
        vgit_log_cb(self.format_with_time('Error -> ' + what))

    def vgit_init(self, path, vgit_log_cb):
        """Log the repository creation"""
        vgit_log_cb(self.format_with_time('Repository created on -> ' + path))

    def vgit_add_all(self, vgit_log_cb):
        """Log that all modified files have been added"""
        vgit_log_cb(self.format_with_time('All files added.'))

    def vgit_ignore_save(self, vgit_log_cb):
        """Log that the .gitignore file as been saved"""
        vgit_log_cb(self.format_with_time('.gitignore saved.'))
