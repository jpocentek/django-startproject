# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.template.defaultfilters import safe
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_avatar',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email')

    def display_avatar(self, obj):
        return safe('<img src="{}" width="24" height="24">'.format(obj.avatar))
    display_avatar.short_description = _("avatar")

admin.site.register(UserProfile, ProfileAdmin)
