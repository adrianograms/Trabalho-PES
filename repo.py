import pygit2


class vgit_repo:
    def vgit_clone(path, url):
        # TODO: report error with call_back
        try:
            pygit2.clone_repository(url, path)
        except pygit2.GitError as err:
            print(err)
