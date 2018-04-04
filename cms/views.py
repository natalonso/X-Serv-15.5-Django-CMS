from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Page

def home(request): #PAGINA PRINCIPAL
    lista = Page.objects.all()
    salida = "Bienvenido al servidor CMS, estas son las paginas disponibles hasta el momento: "
    salida += "<ul>"
    for pagina in lista:
        salida += '<li><a href=' + str(pagina.name) + '>' + pagina.name + '</a>'
    salida += "</ul>"
    print("SALIDA: " + str(salida))
    return HttpResponse(salida)

@csrf_exempt
def pagina(request, pagina):
    if request.method == 'POST':
        newpage= Page(name=request.POST['name'], page=request.POST['page'])
        newpage.save()

    lista = Page.objects.all()
    for elemento in lista:
        if elemento.name == pagina:
            salida = elemento.page
            break
        else:
            salida = None
    if salida == None:
        return HttpResponse('Lo sentimos. La pagina no esta en la base de datos por el momento.')
    else:
        return HttpResponse(salida)
