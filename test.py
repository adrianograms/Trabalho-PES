import unittest
# import vgit
# import repo
import logs


class vgit_logs_test(unittest.TestCase):
    def setUp(self):
        self.logger = logs.vgit_logger('test_log.txt')
        self.url = "test url"
        self.path = "test path"

    def test_vgit_clone_started(self):
        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_clone_started(self.url, self.path, test_cb)

    def test_vgit_clone_finish(self):
        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_clone_finish(test_cb)

    def test_vgit_general_error(self):
        what = "something whent wrong"

        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_general_error(what, test_cb)

    def test_vgit_init(self):
        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_init(self.path, test_cb)


if __name__ == '__main__':
    unittest.main()
