#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:19:18 2019

@author: ericescalante
"""

import os
import re
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    'https://codeup.com/codeups-data-science-career-accelerator-is-here/',
    'https://codeup.com/data-science-myths/',
    'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
    'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
    'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/'
]

def extract_title(codeup_blog_url):
    '''
    Returns the title of a codeup blog url. undefined results with any other url.
    '''
    return re.search(r'.*?([\w-]+)/$', codeup_blog_url)[1]

def fetch_page_text(url):
    response = requests.get(url, headers={'User-Agent': 'Eric'})
    soup = BeautifulSoup(response.text, features="lxml")
    content = soup.find(class_='mk-single-content').text.strip()
    title = extract_title(url)
    return dict(content=content, title=title)

def get_blog_articles(use_cache=True):
    if use_cache and os.path.exists('codeup_blog_articles.json'):
        articles = json.load(open('codeup_blog_articles.json'))
    else:
        articles = [fetch_page_text(url)
                    for url in urls]
        json.dump(articles, open('codeup_blog_articles.json', 'w'))
    return articles

def get_blog_data() -> pd.DataFrame:
    '''
    Returns all the articles from all the sections as a pandas DataFrame
    '''
    return pd.DataFrame(get_blog_articles())
