#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'CED'
SITENAME = u'Certified Edible Dinosaurs'
SHORT_SITENAME = u'CED'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['downloads', 'images']

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

READERS = {'html': None}

THEME = 'themes/dino'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = '{category}-{slug}.html'
ARTICLE_SAVE_AS = '{category}-{slug}.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'


CATEGORY_THUMBNAILS = {
    'hitb-2015-teaser-ctf': 'hitb-2015-teaser-ctf.png',
    'hitb-2016-ctf': 'hitb-2016-ctf.png',
}

MD_EXTENSIONS = [
    'codehilite(css_class=highlight, guess_lang=False, linenums=False)',
    'extra',
]

TYPOGRIFY = True

# Blogroll
LINKS = (('pwnypack', 'https://github.com/edibledinos/pwnypack'),
         ('cuckoo sandbox', 'http://www.cuckoosandbox.org/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags', 'dino']
