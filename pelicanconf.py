#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'itech001'
AUTHORS = u'itech001'
SITENAME = u'ciandcd'
SITEURL = 'http://www.inlicai.com'
#SITESUBTITLE = 'continuous integration and continuous delivery'
SITESUBTITLE = '理财网'

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
DEFAULT_PAGINATION = 20
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_MAX_LENGTH = 0
TYPOGRIFY = False
CACHE_CONTENT = True
CACHE_PATH = 'cache'
PDF_GENERATOR = False
#READERS = {'html': None}
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra/CNAME','extra/robots.txt',]
# path-specific metadata
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'},
    }

#theme
#https://github.com/getpelican/pelican-themes/tree/master/gum
THEME = "themes/bootstrap-spacelab"

#disqus
DISQUS_SITENAME = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ATOM = None
FEED_RSS = 'feeds/rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('itech', 'http://www.cnblogs.com/itech/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/ciandcd'),
          )
#GITHUB_URL = 'https://github.com/ciandcd'
TWITTER_URL = ''
FACEBOOK_URL = ''
GOOGLEPLUS_URL = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#google analytices
GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITENAME = ''
GOOGLE_ANALYTICS_UNIVERSAL = ''


PLUGIN_PATH = ["plugins"]
PLUGINS = ["tag_cloud", "tipue_search"]

#tag_cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
