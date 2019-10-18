import pygit2
from pygit2 import Repository
from pygit2 import RemoteCallbacks


class vgit_repo:
    def vgit_clone(path, url):
        """wraper method for clonnating a
        repository fro a given url to a given path"""
        try:
            pygit2.clone_repository(url, path)
        except pygit2.GitError as err:
            print(err)

    def vgit_init(path, bare=False):
        """wraper method to init a repository in given path"""
        try:
            pygit2.init_repository(path, bare)
        except pygit2.GitError as err:
            print(err)
    
    #This function do the command git add .
    #Path referes to the .git of the repository
    def vgit_add(path):
        try:
            repo = Repository(path)
            index = repo.index
            index.add_all()
            index.write()
        except pygit2.GitError as err:
            print(err)
    
    #This function do the command commit -m "message"
    #Path: is the same of the add, the path to .git of the repository
    #user_name_commiter and email_commiter: informations of the person who gonna do the commit
    #user_name_author and email_author: is the same idea of the commiter but for the author
    #branch: branch which the user want's to do the commit
    #message: message of the coomit
    def vgit_commit(path, user_name_commiter, user_name_author, email_commiter, email_author, branch, message):
        try:
            repo = Repository(path)
            index = repo.index
            reference='refs/heads/' + branch
            tree = index.write_tree()
            author = pygit2.Signature(user_name_author, email_author)
            commiter = pygit2.Signature(user_name_commiter, email_commiter)
            oid = repo.create_commit(reference, author, commiter, message, tree, [repo.head.target])
        except pygit2.GitError as err:
            print(err)
