# [TODO: decidir o nome da ferramenta]
A ferramenta [decidir o nome] tem a finalidade de tornar o uso do git mais fácil e intuitivo.

# Dependências:
#### Gerenciadas pelo pip
##### [PyGit2](https://www.pygit2.org/)
`
$ pip3 install pygit2
`
##### [pyinstaller](https://www.pyinstaller.org/)
`
$ pip3 install pyinstaller
`
    
#### Externas
##### [libgit2](https://libgit2.org/)
##### [GTK+](https://www.gtk.org/)
# 

# Documentação
TODO: link da wiki

# Tecnologias
* Python 3.6 (PyGit2 apenas suporta Python 2.7 e 3.6)
* PyUnit (unittest)

# Features:
| Features              | Backend | GUI |
|:----------------------|:-------:|:---:|
| git-clone             | ❌      | ❌  |
| git-pull              | ️❌      | ️❌  |
| git-push              | ❌️      | ❌  |
| git-init              | ❌️      | ❌  |
| git-merge             | ❌️      | ❌  |
| git-clone             | ❌️      | ❌  |
| git-remote            | ️❌      | ️❌  |
| git-merge             | ❌️      | ❌  |
| git-fetch             | ❌️      | ❌  |
| git-add/remove        | ❌      | ❌  |
| git-commit            | ❌      | ❌  |
| git-reverse           | ❌      | ❌  |
| git-stash             | ❌      | ❌  |
| Historico de commits  | ❌      | ❌  |
| Mudancas nos arquivos | ❌      | ❌  |
| Git credentials       | ❌      | ❌  |
| ShortCuts             | -       | ❌  |
##### Legenda:
❌ = não implementado
✔️ = implementado

# Ferramentas Utilizadas
##### Glade
Ferramenta para o desenvolvimento de GUIs para o GTK+ toolkit.

##### LGTM
Ferramenta de análise de código de maneira automática, e segurança.

# Plataformas Suportadas
* Windows 10
* GNU/Linux

# Inspirado em:
* Magit
