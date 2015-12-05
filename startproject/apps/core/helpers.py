# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string


def random_string(length=8):
    """ Generates alphanumeric random string of given length. """
    return "".join([random.choice(string.letters + string.digits) for x in range(length)])
