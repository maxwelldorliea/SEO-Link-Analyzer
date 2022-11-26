#!/bin/env python3

"""
Link Analyzer Unit Test Module
"""
from crawler import normalize_url
import unittest


class TestLinkAnalyzer(unittest.TestCase):
    """
    Implement All Test Case For The Link Analyzer Module
    """
    def test_normalize_url_with_standard_url(self):
        """
        Test if normalize_url return standard url correctly
        """
        url: str = "https://github.com/maxcarrassco/seo-link-analyzer"
        expect: str = "https://github.com/maxcarrassco/seo-link-analyzer"
        output: str = normalize_url(url)
        self.assertEqual(expect, output)

    def test_normalize_url_with_non_standard_url(self):
        """
        Test if normalize_url return standard url correctly
        """
        url: str = "https://github.com/maxcarrassco/seo-link-analyzer/"
        expect: str = "https://github.com/maxcarrassco/seo-link-analyzer"
        output: str = normalize_url(url)
        self.assertEqual(expect, output)
    
    def test_normalize_url_with_standard_url_with_caps(self):
        """
        Test if normalize_url return standard url correctly
        """
        url: str = "https://Github.coM/Maxcarrassco/Seo-Link-Analyzer"
        expect: str = "https://github.com/maxcarrassco/seo-link-analyzer"
        output: str = normalize_url(url)
        self.assertEqual(expect, output)
    
    def test_normalize_url_with_non_standard_url_with_caps(self):
        """
        Test if normalize_url return standard url correctly
        """
        url: str = "https://Github.coM/Maxcarrassco/Seo-Link-Analyzer/"
        expect: str = "https://github.com/maxcarrassco/seo-link-analyzer"
        output: str = normalize_url(url)
        self.assertEqual(expect, output)
