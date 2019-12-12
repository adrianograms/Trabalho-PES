import time
from singleton import singleton


class vgit_logger(metaclass=singleton):

    def current_time(self):
        return time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())

    def vgit_clone_started(self, url, path, vgit_log_cb):
        """Log when clone has started"""
        log = self.current_time() + ' clonning from -> ' + url + ' ' + 'to -> ' + path

        vgit_log_cb(log)

    def vgit_clone_finish(self, vgit_log_cb):
        """Long when clone has finished """
        log = self.current_time() + ' clone finished'

        vgit_log_cb(log)

    def vgit_general_error(self, what, vgit_log_cb):
        """Log a general error log"""
        log = self.current_time() + ' error -> ' + what

        vgit_log_cb(log)

    def vgit_init(self, path, vgit_log_cb):
        """Log the repository creation"""
        log = self.current_time() + ' repository created on -> ' + path + '\n'

        vgit_log_cb(log)
