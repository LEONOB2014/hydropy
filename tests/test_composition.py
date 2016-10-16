# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:30:01 2016

@author: Marty
"""
from __future__ import absolute_import, print_function

try:
    from unittest import mock
except ImportError:
    import mock
import unittest

import hydropy as hp


class TestStation(unittest.TestCase):

    def test_Station_inits_site(self):
        temp = hp.Station('any')
        actual = temp.site
        expected = 'any'
        self.assertEqual(expected, actual)

    @unittest.skip("Tests of _str_ and _repr_")
    def test_Station_str_returns_str(self):
        temp = hp.Station('any')
        self.assertIsInstance(print(temp), str)

    @mock.patch('hydropy.get_usgs')
    def test_Station_fetch_accepts_source_usgs_iv(self, mock_get):
        expected = 'mock data'
        mock_get.return_value = expected

        actual = hp.Station('any')
        actual.fetch(source='usgs-iv', start='A', end='B')

        mock_get.assert_called_once_with('any', 'iv', 'A', 'B')
        self.assertEqual(expected, actual.data)


class TestAnalysis(unittest.TestCase):

    def test_Analysis_accepts_usgsdv_list(self):
        actual = hp.Analysis(['01585200', '01581500'], source='usgs-dv')
        expected = 'usgs-dv'
        self.assertEqual(expected, actual.source)

    def test_Analysis_accepts_usgsiv_list(self):
        actual = hp.Analysis(['01585200', '01581500'], source='usgs-iv')
        expected = 'usgs-iv'
        self.assertEqual(expected, actual.source)

    def test_Analysis_accepts_dict(self):
        actual = hp.Analysis({'blah':'blah'})
        expected = 'dict'
        self.assertEqual(expected, actual.source)

    def test_Analysis_raises_HydroSourceError_for_bad_source(self):
        with self.assertRaises(hp.HydroSourceError):
            actual = hp.Analysis([1,2,3], source='nonsense')