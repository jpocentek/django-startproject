# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string

from django.conf import settings
from django.contrib.sites.models import Site


def random_string(length=8):
    """ Generates alphanumeric random string of given length. """
    return "".join([random.choice(string.letters + string.digits) for x in range(length)])


def full_uri(path):
    """ Append protocol and domain name for given site path. """
    protocol = 'https' if settings.USE_HTTPS else 'http'
    domain = Site.objects.get_current().domain
    return "{}://{}{}".format(protocol, domain, path)
