# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

import unittest
from whatsupgit.repositoryinfo import RepositoryInfo


class TestRepositoryInfo(unittest.TestCase):
    def setUp(self):
        self.path = '/home/krissi/projects/whatsup-git/.git/'
        self.out = RepositoryInfo(self.path)

    def test_repo_info(self):
        self.assertIsNotNone(self.out)
        self.assertEqual(self.path, self.out.path)

    def test_count(self):
        self.assertTrue(self.out.count_wt_new > 0)