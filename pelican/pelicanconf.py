#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcelo Fonseca Tambalo'
SITENAME = u'Zokis Blog'
SITEURL = 'http://zokis.github.io'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = "/home/znc/projetos/pelican-themes/gum-zokis"

# Blogroll
LINKS = (
    ('Python.org', 'http://python.org/'),
    ('Pelican', 'http://getpelican.com/'),
    ('Django', 'https://www.djangoproject.com/'),
    ('Python Faster Way', 'http://pythonfasterway.uni.me/'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/zokis/'),
    ('Bitbucket', 'https://bitbucket.org/zokis'),
)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
