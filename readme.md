# Whatsup Git?
It searches for git repositories in a given path and shows the number of new, modified and deleted files
in working tree and index


# Dev
## install libgit2 and pygit2
be sure they have the same minor version number

    sudo apt-get install libgit2-dev
    apt-cache policy libgit2-dev
        libgit2-dev:
          Installiert:           **0.19**.0-2
          Versionstabelle:

    virtualenv env
    env/bin/pip install pygit2==0.19
