"""
Vistas
"""
#Django
# libreria importada para hello_world
from django.http import HttpResponse, JsonResponse

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
    # import pdb; pdb.set_trace()

    # tomando los valores de los numbers enviados
    # y obtenidos por get
    if not 'numbers' in request.GET:
        return HttpResponse("NO numbers")

    numbers = request.GET['numbers']
    # transformando string a lista
    numbersList = numbers.split(",")
    numbersInt = []
    # convirtiendo cada valor string de la lista a int
    for i in range(len(numbersList)):
        numbersInt.append(int(numbersList[i]))
    # ordenando esos numeros
    newNumbersInt = sorted(numbersInt)

    # retornando lista ordenada en formato Json
    return JsonResponse({"numbers" : newNumbersInt}, safe=False)
