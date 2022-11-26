#!/bin/env python3

"""
Link Analyzer Crawler Module
"""
from furl import furl
from bs4 import BeautifulSoup as BS
import requests

def normalize_url(url: str) -> str:
    """
    Convert link to standard http form
    """
    url = url.rstrip('/').lower()
    f = furl(url)
    return f.url

def get_urls_from_html(html_str: str, base_url: str) -> list:
    bs = BS(html_str, 'html.parser')
    return bs.find_all('a')
