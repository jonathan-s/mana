#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# from plugins import blogposts

AUTHOR = u'Jonathan'
SITENAME = u'MANA | ANTIRASISTISK TIDSKRIFT'
SITEURL = ''

THEME = 'mana'
PATH = 'content'
ARTICLE_PATH = ['tema']
STATIC_PATHS = ['images', 'fonts']
PLUGINS = ['plugins.blogposts']

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_PAGINATION = 5

# PATTERNS
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'forfattare/{slug}/'
AUTHOR_SAVE_AS = 'forfattare/{slug}/index.html'
AUTHORS_URL = 'forfattare/'
AUTHORS_SAVE_AS = 'forfattare/index.html'

CATEGORY_URL = 'k/{slug}/'
CATEGORY_SAVE_AS = 'k/{slug}/index.html'
CATEGORYS_URL = 'k/'
CATEGORYS_SAVE_AS = 'k/index.html'

# -----------------------------------

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

JINJA_FILTERS = {}  # make a filter for a set.


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
