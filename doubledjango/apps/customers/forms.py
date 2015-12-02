# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('timezone',)
