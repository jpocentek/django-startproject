# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Combined form that allows user also to change his/her user's
    instance first and last name.
    """
    first_name = forms.CharField(max_length=32, label=_("first name"),
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control'}))
    last_name = forms.CharField(max_length=32, label=_("last name"),
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'timezone', 'language',)
        widgets = {
            'timezone': forms.Select(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        obj = super(UserProfileForm, self).save(commit=commit)
        obj.user.first_name = self.cleaned_data['first_name']
        obj.user.last_name = self.cleaned_data['last_name']
        obj.user.save()
        return obj
