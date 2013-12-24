# Whatsup Git?
Do you have too much local git repositories? And you forgot where they are or where you have changed something?
*Whatsup Git* searches for git repositories in a given path and shows the number of new, modified and deleted files
in working tree and index.

# Installation
First install libgit2

    sudo apt-get install libgit2-dev

Than download https://github.com/KrissiK/whatsupgit/releases/download/0.9/whatsupgit-0.9.tar.gz
and run

    pip install whatsupgit-0.9.tar.gz

(tested only on Ubuntu)

# Usage
Run whatsupgit without parameters to search in current directory and below for git repositories. You can specify `-p` parameter to give a path as the start point of the search, e.g.

    whatsupgit -p /home/octocat/projects/


    It returns something like:

    # Git Repositories with changes under: /home/octocat/projects/

    ## /home/octocat/projects/project1 (master)
    ### Working Directory:  New 8  Modified 1

    ## /home/octocat/projects/somethinglarge/proj1 (HEAD)   detached head
    ### No changes

    ## /home/octocat/projects/somethinglarge/proj2 (master)
    ### Working Directory:  New 1

    ## /home/octocat/projects/gitolite-admin-old (HEAD)   detached head
    ### Working Directory:  New 9 Deleted 2
    ### Index            :  New 2 Modified 8

# As git alias
If you want to use `git whatsup` as an alias for whatsupgit you can add this to your ~/.gitconfig

    [alias]
        whatsup = !sh -c 'whatsupgit'

Now you can run

    git whatsup

to find all git repositories at your current path.