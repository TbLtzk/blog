#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tobias Latzke'
SITENAME = u'BLOGchain'
SITESUBTITLE = 'by Tobias Latzke'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Centaurus', 'https://play.google.com/store/apps/details?id=de.xcoins.centaurus'),
         ('Stellar.org Mandate', 'https://www.stellar.org/about/mandate/'),
        )

# Social widget
SOCIAL = (
	('twitter', 'https://twitter.com/TbLtzk'),
	('github', 'http://github.com/TbLtzk'),
	('linkedin', 'https://de.linkedin.com/in/tobias-latzke-645269a3'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
