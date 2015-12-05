# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from slugify import slugify

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile


class LoginForm(forms.Form):
    """ Custom login form that requires email instead of username.
    """
    email = forms.EmailField(label=_("email"), widget=forms.EmailInput(attrs={
                                    'class': 'form-control'},))
    password = forms.CharField(label=_("password"), max_length=32,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',}))

    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        if not valid:
            return False
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except ObjectDoesNotExist:
            return False
        auth_user = authenticate(username=user.username,
                                 password=self.cleaned_data['password'])
        if auth_user is None or not auth_user.is_active:
            return False
        self.instance = auth_user
        return True


class RegisterForm(UserCreationForm):
    """ Extended user creation form providing slugified username. """
    email = forms.EmailField(label=_("email"),
                             widget=forms.EmailInput(
                                attrs={'class': 'form-control'}))
    first_name = forms.CharField(label=_("first name"),
                                 widget=forms.TextInput(
                                    attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_("last name"),
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=_("password"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=_("repeat password"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(_('Email address already taken'))
        return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        f_name = self.cleaned_data['first_name']
        l_name = self.cleaned_data['last_name']
        username = slugify("{}-{}".format(f_name, l_name))
        final_username = username
        retries = 0
        success = False
        while not success:
            try:
                User.objects.get(username=final_username)
                retries += 1
                final_username = "{}-{}".format(username, retries)
            except User.DoesNotExist:
                user.username = final_username
                success = True
        if commit:
            user.save()
        return user


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
