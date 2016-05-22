#!/usr/bin/env python
#coding:utf-8
import sys
import imp
if sys.getdefaultencoding()=='ascii':
    imp.reload(sys)
    sys.setdefaultencoding('utf-8')

from django.apps import AppConfig

class SiteApp(AppConfig):
    name = "site"
