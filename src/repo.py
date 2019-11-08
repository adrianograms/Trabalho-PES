import pygit2
from pygit2 import Repository


class vgit_repo:
    def vgit_clone(path, url):
        """wraper method for clonnating a
        repository from a given `url' to a given `path'"""
        try:
            pygit2.clone_repository(url, path)
        except pygit2.GitError as err:
            print(err)

    def vgit_init(path, bare=False):
        """wraper method to init a repository in given `path'"""
        try:
            pygit2.init_repository(path, bare)
        except pygit2.GitError as err:
            print(err)

    def vgit_add(path):
        """ This function do the command git add
        `path' referes to the .git of the repository """
        try:
            repo = Repository(path)
            index = repo.index
            index.add_all()
            index.write()
        except pygit2.GitError as err:
            print(err)

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
