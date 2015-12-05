# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.flatpages.models import FlatPage
from django.contrib.sitemaps import Sitemap


class FlatPageSitemap(Sitemap):

    def items(self):
        return FlatPage.objects.all()


sitemaps = {'flatpages': FlatPageSitemap,}
