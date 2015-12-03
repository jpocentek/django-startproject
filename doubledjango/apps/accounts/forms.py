# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)
