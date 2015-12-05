# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic.edit import UpdateView

from ..core.views import LoginRequiredMixin
from .forms import UserProfileForm
from .models import UserProfile


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
