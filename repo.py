import pygit2


class vgit_repo:
    def vgit_clone(path, url):
        # TODO: add error check here
        pygit2.clone_repository(url, path)
