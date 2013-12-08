# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

import unittest
from whatsupgit.repositoryinfo import RepositoryInfo
import sh
import os
import shutil


class TestRepositoryInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_path = "/tmp"
        repo_name = "Spoon-Knife"
        cls.repo_path = os.path.join(base_path, repo_name)
        if os.path.exists(cls.repo_path):
            shutil.rmtree(cls.repo_path)
        git = sh.git.bake(_cwd=base_path)
        git.clone('https://github.com/KrissiK/Spoon-Knife.git')

    def setUp(self):
        git = sh.git.bake(_cwd=self.__class__.repo_path)
        git.reset('7f4505682033eda1aa5771cf7faa7fabdfb32172', '--hard')
        git.clean('-f')  # remove all files from Working Tree that are not in commit 7f45
        self.git = git
        self.repo_under_test = RepositoryInfo(self.__class__.repo_path)

    def test_head_name(self):
        self._create_new_file_in_working_tree()
        self.assertIn('test.txt', self.git.status())
        self.assertEqual('master', self.repo_under_test.get_current_branch_name())

    def test_head_name_switchedBranch(self):
        self.git.checkout('-b', 'development')
        self.assertEqual('development', self.repo_under_test.get_current_branch_name())

    def test_path(self):
        self.assertIsNotNone(self.repo_under_test)
        self.assertEqual(self.repo_path, self.repo_under_test.path)

    def test_count(self):
        self.assertTrue(self.repo_under_test.count_wt_new == 0)
        self._create_new_file_in_working_tree()
        self.repo_under_test = RepositoryInfo(self.__class__.repo_path)  # RepositoryInfo-Object created before
                                                                         # new file in working tree
                                                                         # => create new RepositoryInfo (or call _count)
        self.assertTrue(self.repo_under_test.count_wt_new == 1)

    def _create_new_file_in_working_tree(self, file_name='test.txt', content='hallo welt'):
        path = os.path.join(self.__class__.repo_path, file_name)
        new_file = open(path, 'w+')
        new_file.write(content)
        new_file.close()