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
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    now = str(now)
    data = 'Hello Django :) Its {0}'.format(now)
    return HttpResponse(data)

def hi(request):
    """Hi function"""
    # print("Hi request object:{0}".format(request))
    import pdb; pdb.set_trace()
    return HttpResponse("Hi")
