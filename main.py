# -*- coding: utf-8 -*-
__author__ = 'kuche'

from pygit2 import (discover_repository,
                    Repository,
                    GIT_STATUS_CURRENT,
                    GIT_STATUS_INDEX_NEW,
                    GIT_STATUS_INDEX_MODIFIED,
                    GIT_STATUS_INDEX_DELETED,
                    GIT_STATUS_WT_NEW,
                    GIT_STATUS_WT_MODIFIED,
                    GIT_STATUS_WT_DELETED
                    )
import os

#repo_path = discover_repository("/usr/local/home/kuche/plone-migration/plone4-buildout")
startpath = "/home/krissi/projects"
for p in os.listdir(startpath):
    print "# %s" % p
    try:
        repo_path = discover_repository(startpath + "/" + p)
    except KeyError:
        pass
    else:
        repo = Repository(repo_path)
        status = repo.status()
        wt_modified_counter = 0
        wt_new_counter = 0
        index_new_counter = 0
        index_modified_counter = 0
        for filepath, flags in status.items():
            if flags != GIT_STATUS_CURRENT:
                if flags == GIT_STATUS_WT_MODIFIED:
                    wt_modified_counter += 1
                if flags == GIT_STATUS_WT_NEW:
                    wt_new_counter += 1
                if flags == GIT_STATUS_INDEX_NEW:
                    index_new_counter += 1
                if flags == GIT_STATUS_INDEX_MODIFIED:
                    index_modified_counter += 1

        print "## %s " % repo_path
        print "### %s" % status
        print "#### modified:       %s" % wt_modified_counter
        print "#### new:            %s" % wt_new_counter
        print "#### index new:      %s" % index_new_counter
        print "#### index modified: %s" % index_modified_counter
