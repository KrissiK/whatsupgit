# install libgit2 and pygit 
be sure they have the same minor version number

    sudo apt-get install libgit2-dev
    apt-cache policy libgit2-dev
        libgit2-dev:
          Installiert:           **0.19**.0-2
          Versionstabelle:

    virtualenv env
    env/bin/pip install pygit2==0.19
