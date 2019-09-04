from time import gmtime, strftime


class vgit_logger:
    def __init__(self):
        with open('log/vgit_logs.txt', 'r') as file:
            content = file.readlines()
            file.close()

        self.logs = [line for line in content]

    def vgit_load_logs(self, vgit_log_cb):
        for line in self.logs:
            vgit_log_cb(line)

    def vgit_close_logs(self):
        with open('log/vgit_logs.txt', 'w') as file:
            file.writelines(self.logs)
            file.close()

    def vgit_clone_started(self, url, path, vgit_log_cb):
        time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())

        self.log = time + ' clonning from -> ' + url + ' ' + 'to -> ' + path + '\n'
        self.logs.append(self.log)

        vgit_log_cb(self.log)

    def vigt_clone_finish(self, vgit_log_cb):
        time = strftime("[%Y-%m-%d %H:%M:%S]", gmtime())

        self.log = time + ' clone finished' + '\n'
        self.logs.append(self.log)

        vgit_log_cb(self.log)
