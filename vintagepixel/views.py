"""
Vistas
"""
#Django
# libreria importada para hello_world
from django.http import HttpResponse

#utilities
from datetime import datetime

def hello_world(request):
    """
    El requet es obligatorio
    """
    now = datetime.now().strftime('%b %d %Y - %H:%M hrs')
    now = str(now)
    data = 'Hello Django :) Its {0}'.format(now)
    return HttpResponse(data)
