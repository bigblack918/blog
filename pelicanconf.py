#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Leo Tsai'
SITENAME = "Leo's Blog"
SITEURL = 'http://leo.nctu.me/'
#SITEURL = 'http://0.0.0.0:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer'
#FAVICON = '/images/favicon.ico'
PYGMENTS_STYLE = 'monokai'

PATH = 'content'

# Times and dates.
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'en'

# Set the article URL.
ARTICLE_URL = 'blog/{date:%Y%m%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y%m%d}/{slug}/index.html'

# Search
SEARCH_BOX = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
#HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
#LINKS = (('GitHup', 'https://github.com/bigblack918/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/leotsai918'),
          ('github', 'https://github.com/bigblack918/'),)

# Title menu options.
MENUITEMS = [('Categories', '%s/categories.html' % SITEURL),
             ('Archives', '%s/archives.html' % SITEURL),
             #('Tags', '%s/tags.html' % uri),
             ]

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'extra']
DISPLAY_CATEGORIES_ON_MENU = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'FLEX'
DISQUS_SITENAME = 'leotsai'
GOOGLE_ANALYTICS = 'UA-109186019-1'


## Config google sitemap 
PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}