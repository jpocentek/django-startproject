# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def handler500(request):
    """ Use custom template for critical error responses.
    """
    response = render_to_response('500.html', {},
                context_instance=RequestContext(request))
    response.status_code = 500
    return response


class LoginRequiredMixin(object):
    """ Ensures that user must be authenticated in order to access view.
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
