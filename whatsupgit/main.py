# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

from repofinder import RepositoryFinder
from repositoryinfo import RepositoryInfo
from repositoryinfoprinter import RepositoryInfoPrinter

def main():
    start_dir = '/home/krissi/projects/'
    finder = RepositoryFinder(start_dir)
    repo_paths = finder.find()
    repo_infos = []
    for r in repo_paths:
        repo_infos.append(RepositoryInfoPrinter(RepositoryInfo(r)))

    for r in repo_infos:
        r.print_info()

if __name__ == "__main__":
    main()
