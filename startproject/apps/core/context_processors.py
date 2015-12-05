from django.conf import settings

def debug_processor(request):
    """ Return DEBUG value from settings file. """
    return {'DEBUG': settings.DEBUG,}
