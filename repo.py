import pygit2


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
