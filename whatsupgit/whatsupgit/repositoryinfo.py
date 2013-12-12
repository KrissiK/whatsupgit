# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

from pygit2 import (Repository,
                    GIT_STATUS_CURRENT,
                    GIT_STATUS_INDEX_NEW,
                    GIT_STATUS_INDEX_MODIFIED,
                    GIT_STATUS_INDEX_DELETED,
                    GIT_STATUS_WT_NEW,
                    GIT_STATUS_WT_MODIFIED,
                    GIT_STATUS_WT_DELETED
                    )


class RepositoryInfo(object):
    """ wraps an pygit2.Repository object
    """

    def __init__(self, repo_path):
        self._repo = Repository(repo_path)
        self.count_unmodified = 0
        self.count_wt_modified = 0
        self.count_wt_new = 0
        self.count_wt_deleted = 0
        self.count_index_modified = 0
        self.count_index_new = 0
        self.count_index_deleted = 0
        self._count()

    @property
    def path(self):
        sep = '/'
        splitted = self._repo.path.split(sep)[0:-2]
        return sep.join(splitted)

    @property
    def has_workingtree_changes(self):
        return self.count_wt_deleted > 0 or self.count_wt_modified > 0 or self.count_wt_new > 0

    @property
    def has_index_changes(self):
        return self.count_index_deleted > 0 or self.count_index_modified > 0 or self.count_index_new > 0

    def _count(self):
        _status = self._repo.status()
        for file_path, flags in _status.items():
            if flags == GIT_STATUS_CURRENT:
                self.count_unmodified += 1
            elif flags == GIT_STATUS_WT_MODIFIED:
                self.count_wt_modified += 1
            elif flags == GIT_STATUS_WT_NEW:
                self.count_wt_new += 1
            elif flags == GIT_STATUS_INDEX_NEW:
                self.count_index_new += 1
            elif flags == GIT_STATUS_INDEX_MODIFIED:
                self.count_index_modified += 1
            elif flags == GIT_STATUS_INDEX_DELETED:
                self.count_index_deleted += 1
            elif flags == GIT_STATUS_WT_DELETED:
                self.count_wt_deleted += 1

    @property
    def current_branch_name(self):
        # ToDo: Why does self._repo.head.shorthand not work?
        head = self._repo.head
        head_name = head.name.split('/')[-1:]
        return head_name[0]

    @property
    def is_head_upstream_branch(self):
        """ determines if current head is the same commit as the remote commit
        """
        if self._repo.head_is_detached:
            return False
        current_branch_name = self.current_branch_name
        head = self._repo.head
        remote_branch = self._repo.lookup_branch(current_branch_name).upstream
        if remote_branch:
            return remote_branch.target.hex == head.target.hex
        return False

    @property
    def is_head_detached(self):
        return self._repo.head_is_detached