# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import UpdateView

from ..core.views import LoginRequiredMixin
from .forms import CustomerForm
from .models import Customer


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """ Let currently existed user edit his/her Customer instance.
    """
    model = Customer
    form_class = CustomerForm

    def get_object(self):
        try:
            return self.request.user.customer
        except ObjectDoesNotExist:
            raise Http404
