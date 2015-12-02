# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytz

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


@python_2_unicode_compatible
class Customer(models.Model):
    """ Extends native User model with one-to-one relation.
    """
    TIMEZONE_CHOICES = [(x, x) for x in pytz.common_timezones_set]

    user = models.OneToOneField(User, verbose_name=_("user"))
    timezone = models.CharField(_("timezone"), max_length=64,
                                choices=TIMEZONE_CHOICES,
                                default=settings.TIMEZONE)
    language = models.CharField(_("language"), max_length=2,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def __str__(self):
        return self.user.get_full_name()
