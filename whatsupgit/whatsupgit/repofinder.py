# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'
import os
from pygit2 import (discover_repository,
                    )


class RepositoryFinder(object):

    def __init__(self, start_directory):
        self.start_dir = start_directory

    def find(self):
        """finds all repositories and return their paths
        """
        found = set()
        for dir_name, dir_names, file_names in os.walk(self.start_dir):
            git_dir = ""
            try:
                if '.git' in dir_name.split(os.sep)[-1:]:
                    git_dir = dir_name + os.sep
                    del dir_names[:]  # do not go to subdirs
            except KeyError:
                pass
            if not git_dir == '':
                found.add(git_dir)

            # don't go into hidden directories.
            hidden_dirs = filter(lambda name: name.startswith('.') and not '.git' == name, dir_names)
            for hidden_dir in hidden_dirs:
                dir_names.remove(hidden_dir)

        return found