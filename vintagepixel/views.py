"""
Vistas
"""
# libreria importada para hello_world
from django.http import HttpResponse

def hello_world(request):
    """
    El requet es obligatorio
    """
    return HttpResponse('Hello Django :)')
