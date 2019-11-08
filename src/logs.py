import time


class vgit_logger:
    def __init__(self, default_logs='log/vgit_logs.txt'):
        self.logs_path = default_logs

        with open(self.logs_path, 'r') as file:
            content = file.readlines()

            self.logs = [line for line in content]

    def current_time(self):
        return time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())

    def vgit_load_logs(self, vgit_log_cb):
        """load_the_logs when the program starts"""
        for line in self.logs:
            vgit_log_cb(line)

    def vgit_close_logs(self):
        """save the logs when the program closes"""
        with open(self.logs_path, 'w') as file:
            file.writelines(self.logs)
            file.close()

    def vgit_clone_started(self, url, path, vgit_log_cb):
        """log when clone has started"""
        log = self.current_time() + ' clonning from -> ' + url + ' ' + 'to -> ' + path + '\n'
        self.logs.append(log)

        vgit_log_cb(log)

    def vgit_clone_finish(self, vgit_log_cb):
        """log when clone has finished """
        log = self.current_time() + ' clone finished' + '\n'

        self.logs.append(log)

        vgit_log_cb(log)

    def vgit_general_error(self, what, vgit_log_cb):
        """general error log"""
        self.logs.append(what)
        vgit_log_cb(what)

    def vgit_init(self, path, vgit_log_cb):
        """vgit inti log"""
        log = self.current_time() + ' repository created on -> ' + path + '\n'
        self.logs.append(log)

        vgit_log_cb(log)
