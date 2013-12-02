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
                git_dir = discover_repository(dir_name)
            except KeyError:
                pass
            else:
                found.add(git_dir)
            if '.git' in dir_names:
                # don't go into any .git directories.
                dir_names.remove('.git')

        return found