import pygit2

from pygit2 import Repository
from singleton import singleton


class vgit_repo(metaclass=singleton):
    def __init__(self):
        self.repo = None

    def vgit_load_repo(self, path):
        if path is None:
            self.repo = None
            return
        try:
            self.repo = Repository(path)
        except ValueError:
            self.repo = None
        except Exception:
            self.repo = None

    def vgit_clone(self, path, url, log_cb):
        """Wraper method to clone a
        repository from a given `url' to a given `path'"""
        try:
            pygit2.clone_repository(url, path)
        except ValueError as err:
            log_cb(str(err))
            return False
        except Exception as err:
            log_cb(str(err))
            return False

        return True

    def vgit_init(self, path, log_cb, bare=False):
        """Wraper method to init a repository in given `path'"""
        try:
            pygit2.init_repository(path, bare)
        except ValueError as err:
            log_cb(str(err))
            return False
        except Exception as err:
            log_cb(str(err))
            return False

        return True

    def vgit_add_all(self, log_cb):
        """Wraper method to add all files to a commit."""
        try:
            if self.repo is None:
                log_cb("No .git in current directory. Use `init' to crete a new repository.")
                return False

            self.repo.index.add_all()
            self.repo.index.write()

        except ValueError as err:
            log_cb(str(err))
            return False
        except Exception as err:
            log_cb(str(err))
            return False

        return True

    def vgit_commit(self, user_name, email, branch, message, log_cb):
        """Wraper method for the commit -m "message" git command. `user_name' and
        `email' informations of the autor of the commit
        `user_name_author' and email_author: is the same idea of the
        commiter but for the author `branch' branch which the user
        want's to do the commit `message': message of the commit"""

        try:
            if self.repo is None:
                log_cb("No .git in current directory. Use `init' to crete a new repository.")
                return False

            reference = 'refs/heads/' + branch
            author = pygit2.Signature(user_name, email)
            # usando author e commiter como o mesmo ser
            self.repo.create_commit(reference, author, author, message,
                                    self.repo.TreeBuilder().write(),
                                    [self.repo.head.target])

        except ValueError as err:
            log_cb(str(err))
            return False
        except Exception as err:
            log_cb(str(err))
            return False

        return True

    def vgit_commits(self, log_cb):
        if self.repo is None:
            log_cb("No commits...")
        else:
            for commit in self.repo.walk(self.repo[self.repo.head.target].id,
                                         pygit2.GIT_SORT_TIME):
                log_cb('\n'.join(['Commit: #{}'.format(commit.tree_id.hex),
                                  'Author: {} <{}>'.format(commit.author.name,
                                                           commit.author.email),
                                  'Message: ',
                                  commit.message,
                                  '']))

    def vgit_push(self, path, message, user_name_commiter, user_name_author,
                  email_commiter, email_author, branch,
                  user_name_pusher, user_passoword_pusher,
                  log_cb):
        try:
            repo = Repository(path)
            index = repo.index
            reference='refs/heads/' + branch
            tree = index.write_tree()
            author = pygit2.Signature(user_name_author, email_author)
            commiter = pygit2.Signature(user_name_commiter, email_commiter)
            oid = repo.create_commit(reference, author, commiter, message, tree, [repo.head.target])
            credentials = pygit2.UserPass(user_name_pusher,user_passoword_pusher)
            remo = repo.remotes["origin"]
            remo.credentials = credentials
            aux = remo.url
            repo.remotes.set_push_url(user_name_pusher,aux)
            callbacks = pygit2.RemoteCallbacks(credentials=credentials)
            remo.push([reference],callbacks=callbacks)

        except ValueError as err:
            log_cb(str(err))
            return False
        except Exception as err:
            log_cb(str(err))
            return False

        return True
