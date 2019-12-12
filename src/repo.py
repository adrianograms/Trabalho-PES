import pygit2

from pygit2    import Repository
from singleton import singleton

class vgit_repo(metaclass=singleton):
    def __init__(self, path=None):
        if path is None:
            self.repo = None
            return

        try:
            self.repo = Repository(path)
        except pygit2.GitError as err:
            self.repo = None
        except pygit2.AlreadyExistsError as err:
            self.repo = None
        except pygit2.InvalidSpecError as err:
            self.repo = None

    def vgit_clone(self, path, url, log_cb):
        """Wraper method to clone a
        repository from a given `url' to a given `path'"""
        try:
            pygit2.clone_repository(url, path)
        except pygit2.GitError as err:
            log_cb(err)
        except pygit2.AlreadyExistsError as err:
            log_cb(err)
        except pygit2.InvalidSpecError as err:
            log_cb(err)


    def vgit_init(self, path, log_cb, bare=False):
        """Wraper method to init a repository in given `path'"""
        try:
            pygit2.init_repository(path, bare)
        except pygit2.GitError as err:
            log_cb(err)
        except pygit2.AlreadyExistsError as err:
            log_cb(err)
        except pygit2.InvalidSpecError as err:
            log_cb(err)

    def vgit_add(self, log_cb):
        """Wraper method to add all files to a commit."""
        try:
            if self.repo is None:
                log_cb("Could not find the .git file in the current directory")
                return False

            self.repo.index.add_all()
            self.repo.index.write()

        except pygit2.GitError as err:
            log_cb(err)
        except pygit2.AlreadyExistsError as err:
            log_cb(err)
        except pygit2.InvalidSpecError as err:
            log_cb(err)


            # TODO: fix
    def vgit_commit(path, user_name_commiter, user_name_author,
                    email_commiter, email_author, branch, message):
        """This function do the command commit -m "message" `path' is the the
        path to .git of the repository `user_name_commiter' and
        `email_commiter' informations of the autor of the commit
        `user_name_author' and email_author: is the same idea of the
        commiter but for the author `branch' branch which the user
        want's to do the commit `message': message of the commit"""

        try:
            repo = Repository(path)
            index = repo.index
            reference = 'refs/heads/' + branch
            tree = index.write_tree()
            author = pygit2.Signature(user_name_author, email_author)
            commiter = pygit2.Signature(user_name_commiter, email_commiter)
            repo.create_commit(reference, author, commiter,
                               message, tree, [repo.head.target])
        except pygit2.GitError as err:
            print(err)
