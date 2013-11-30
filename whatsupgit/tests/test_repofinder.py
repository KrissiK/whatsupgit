# -*- coding: utf-8 -*-
__author__ = 'Kristin Kuche'

import unittest
from whatsupgit.repofinder import RepositoryFinder


class TestRepoFinder(unittest.TestCase):

    def setUp(self):
        self.out = RepositoryFinder('/home/krissi/projects')

    def test_finder(self):
        result = self.out.find()
        self.assertTrue(len(result) > 0)
        for r in result:
            print r