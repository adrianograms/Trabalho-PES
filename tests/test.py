import unittest
import os
import sys
sys.path.append('../src/')

from src import logs
from src import repo

class vgit_logs_test(unittest.TestCase):
    def setUp(self):
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
        what = ""

        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_general_error(what, test_cb)

    def test_vgit_init(self):
        def test_cb(log):
            self.assertEqual(log, self.logger.logs[0])

        self.logger.vgit_init(self.path, test_cb)


class vgit_inti_test(unittest.TestCase):
    def setUp(self):
        os.system('mkdir init_test')
        os.system('cd init_test')


    def cleanUp(self):
        os.system('cd ..')
        os.system('rm -rf init_test')


if __name__ == '__main__':
    unittest.main(verbosity=2)
