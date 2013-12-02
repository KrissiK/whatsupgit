# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

from repofinder import RepositoryFinder
from repositoryinfo import RepositoryInfo
from repositoryinfoprinter import RepositoryInfoPrinter
from optparse import OptionParser, Option
import os

def main():
    parser = OptionParser()
    parser.add_option("-p", "", dest='path', help="Please specify path.",default='')
    (options, args) = parser.parse_args()
    start_dir = options.path or os.getcwd()
    print "# Git Repositories with changes under: " + start_dir
    finder = RepositoryFinder(start_dir)
    repo_paths = finder.find()
    repo_infos = []
    for r in repo_paths:
        repo_infos.append(RepositoryInfoPrinter(RepositoryInfo(r)))

    for r in repo_infos:
        r.print_info()

if __name__ == "__main__":
    main()
