# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytz

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL


def get_timezone_choices():
    """ Show unique timezones in sorted order. """
    return [(x, x) for x in sorted(list(pytz.common_timezones_set))]


@python_2_unicode_compatible
class UserProfile(models.Model):
    """ Extends native User model with one-to-one relation.
    """
    user = models.OneToOneField(User, verbose_name=_("user"),
                                related_name="profile")
    timezone = models.CharField(_("timezone"), max_length=64,
                                choices=get_timezone_choices(),
                                default=settings.TIME_ZONE)
    language = models.CharField(_("language"), max_length=2,
                                choices=settings.LANGUAGES,
                                default=settings.LANGUAGE_CODE)

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    def __str__(self):
        return self.user.get_full_name()
