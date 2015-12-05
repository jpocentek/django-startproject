# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth, messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView, UpdateView

from ..core.views import LoginRequiredMixin
from .forms import LoginForm, RegisterForm, UserProfileForm
from .models import UserProfile


class AuthFormMixin(FormView):
    """ Mixin providing success url for auth views using 'next' parameter.
    """
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(AuthFormMixin, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url is not None:
            return next_url
        return settings.LOGIN_REDIRECT_URL


class LoginView(AuthFormMixin):
    """ Use custom form for user authorization process.
    """
    template_name = "registration/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        auth.login(self.request, form.instance)
        UserProfile.objects.get_or_create(user=form.instance)
        return super(LoginView, self).form_valid(form)


class RegisterView(AuthFormMixin):
    """ Use custom form for user registration.
    """
    template_name = "registration/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, _("Registration successfull"))
        return super(RegisterView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Let currently authorized user edit his/her Customer instance.
    """
    model = UserProfile
    form_class = UserProfileForm

    def get_object(self):
        try:
            return self.request.user.profile
        except ObjectDoesNotExist:
            raise Http404

    def get_success_url(self):
        return reverse('accounts:profile')

    def form_valid(self, form):
        messages.success(self.request, _("Settings saved"))
        return super(ProfileUpdateView, self).form_valid(form)
