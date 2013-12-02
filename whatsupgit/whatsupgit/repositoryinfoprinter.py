# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class RepositoryInfoPrinter(object):
    """prints information of a repository
    """

    def __init__(self, repo_info, show_all=False):
        self.repo_info = repo_info

    def print_info(self):
        c_wt_n = self.repo_info.count_wt_new
        c_wt_m = self.repo_info.count_wt_modified
        c_wt_d = self.repo_info.count_wt_deleted
        c_i_n = self.repo_info.count_index_new
        c_i_m = self.repo_info.count_index_modified
        c_i_d = self.repo_info.count_index_deleted

        if not self.repo_info.has_workingtree_changes and not self.repo_info.has_index_changes:
            return

        print "\n## %s" % self.repo_info.path

        template = "%(color_new)s New %(new)s %(color_end)s" + \
                   " %(color_modified)s Modified %(modified)s %(color_end)s" + \
                   " %(color_del)s Deleted %(del)s %(color_end)s"
        if self.repo_info.has_workingtree_changes:
            print "### Working Directory: " + \
                  template % {'new': c_wt_n,
                              'modified': c_wt_m,
                              'del': c_wt_d,
                              'color_new': bcolors.OKGREEN,
                              'color_modified': bcolors.OKBLUE,
                              'color_del': bcolors.FAIL,
                              'color_end': bcolors.ENDC,
                              }

        if self.repo_info.has_index_changes:
            print "### Index            : " + \
            template % {'new': c_i_n,
                        'modified': c_i_m,
                        'del': c_i_d,
                        'color_new': bcolors.OKGREEN,
                        'color_modified': bcolors.OKBLUE,
                        'color_del': bcolors.FAIL,
                        'color_end': bcolors.ENDC,
                        }