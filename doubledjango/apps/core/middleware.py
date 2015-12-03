# -*- coding: utf-8 -*-
import pytz

from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone, translation


class TimezoneMiddleware(object):
    """
    Set current timezone for user based either on his personal settings or
    fetched from session data (may be set by JS scripts, as this is more
    accurate method in this case).
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            try:
                tzname = request.user.profile.timezone
            except ObjectDoesNotExist:
                tzname = None
        else:
            tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()


class LanguageMiddleware(object):
    """
    Adjust language settings based on user profile preferences.
    """
    def process_request(self, request):
        language = None
        if request.user.is_authenticated():
            try:
                language = request.user.profile.language
            except ObjectDoesNotExist:
                langugage = None
        if translation.check_for_language(language):
            translation.activate(language)
