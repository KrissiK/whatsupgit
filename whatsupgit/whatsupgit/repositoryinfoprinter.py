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
        self.c_wt_n = self.repo_info.count_wt_new
        self.c_wt_m = self.repo_info.count_wt_modified
        self.c_wt_d = self.repo_info.count_wt_deleted
        self.c_i_n = self.repo_info.count_index_new
        self.c_i_m = self.repo_info.count_index_modified
        self.c_i_d = self.repo_info.count_index_deleted

    def print_info(self):

        if not self.repo_info.has_workingtree_changes and not self.repo_info.has_index_changes:
            self._print_headline()
            print "### No changes"
            return

        self._print_headline()
        self._print_working_dir_changes()
        self._print_index_changes()
        print self.repo_info.last_tag
        print "#-#" * 10

    @classmethod
    def _get_colors(cls):
        return {'color_new': bcolors.OKGREEN,
                'color_modified': bcolors.OKBLUE,
                'color_del': bcolors.FAIL,
                'color_end': bcolors.ENDC,
                'color_highlight': bcolors.WARNING,
                'color_end': bcolors.ENDC,
                'color_push': bcolors.HEADER,
        }

    def _print_headline(self):
        colors = self._get_colors()
        needs_push = self.repo_info.is_head_upstream_branch
        push = ''
        if not needs_push:
            push = ' pushable'

        detached_head = self.repo_info.is_head_detached
        if detached_head:
            push = ' detached head'

        headline = "\n## %(repo_path)s (%(color_highlight)s%(repo_current_branch)s%(color_end)s)"\
                   + "  %(color_push)s%(push)s %(color_end)s"
        headline_data = {'repo_path': self.repo_info.path,
                         'repo_current_branch': self.repo_info.current_branch_name,
                         'push': push,
                         }
        headline_data.update(colors)
        print headline % headline_data

    def _print_working_dir_changes(self):
        if self.repo_info.has_workingtree_changes:
            print "### Working Directory: " + self._get_changes_as_colored_string(self.c_wt_n, self.c_wt_m, self.c_wt_d)

    def _print_index_changes(self):
        if self.repo_info.has_index_changes:
            print "### Index            : " + self._get_changes_as_colored_string(self.c_i_n, self.c_i_m, self.c_i_d)

    def _get_changes_as_colored_string(self, count_new, count_modified, count_deleted):
        template = ""
        if count_new > 0:
            template += "%(color_new)s New %(new)s %(color_end)s"
        if count_modified > 0:
            template += "%(color_modified)s Modified %(modified)s %(color_end)s"
        if count_deleted > 0:
            template += "%(color_del)s Deleted %(del)s %(color_end)s"

        data = {'new': count_new,
                'modified': count_modified,
                'del': count_deleted,
                }
        data.update(self._get_colors())
        return template % data
