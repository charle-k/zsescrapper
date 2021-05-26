from django.shortcuts import render
from django.http import HttpResponse

from .utils import get_zse_data


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def checkzse(request):
    zse_data, sale_date = get_zse_data()
    print('ZSE Sale Date =>', sale_date)
    return render(request, 'spider/checkzse.html', {'zse_data': zse_data, 'sale_date': sale_date})

# Create your views here.
