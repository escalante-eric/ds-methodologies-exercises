#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:19:18 2019

@author: ericescalante
"""

import os
import json
import itertools as it
from typing import List, Dict

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = 'https://inshorts.com/en/read'
SECTIONS = ['business', 'sports', 'technology', 'entertainment']

def handle_article(article: BeautifulSoup) -> Dict[str, str]:
    '''
    Given a single article, extracts the title and content
    '''
    return {
        'title': article.find(class_='repo-list').find('a').text.strip(),
        'content': (article.find(class_='news-card-content')
                    .find('div', attrs={'itemprop': 'articleBody'})
                    .text.strip())
    }

def fetch_section(section: str) -> List[Dict[str, str]]:
    '''
    Makes a request for the given section and processes all the articles in it
    '''
    url = f'{BASE_URL}/{section}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    articles = [handle_article(article) for article in soup.find_all(class_='news-card')]
    for article in articles:
        article['category'] = section
        
    return articles

def get_all_sections() -> List[Dict[str, str]]:
    '''
    Returns the processed article data for all of the sections we defined in
    SECTIONS
    '''
    sections = [fetch_section(section) for section in SECTIONS]

    return list(it.chain(*sections))

def get_news_articles(use_cache=True) -> List[Dict[str, str]]:
    if use_cache and os.path.exists('news_articles.json'):
        articles = json.load(open('news_articles.json'))
    else:
        articles = get_all_sections()
        json.dump(articles, open('news_articles.json', 'w'))
        
    return articles

def get_news_data() -> pd.DataFrame:
    '''
    Returns all the articles from all the sections as a pandas DataFrame
    '''
    return pd.DataFrame(get_all_sections())







