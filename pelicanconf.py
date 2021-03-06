#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergio Rey'
SITENAME = u'Geographic Information Analysis'
SITEURL = ''

HIDE_SIDEBAR = True

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs', 'figures', 'data']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'themes/pelican-bootstrap3'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False
#
#MENUITEMS = (('Syllabus', 'syllabus.html'), ('Schedule', 'schedule.html'))

CC_LICENSE = 'CC-BY'
