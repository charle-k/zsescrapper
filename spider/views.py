import json

from django.shortcuts import render
from django.http import HttpResponse

from .utils import get_zse_data
from .models import ZSEData


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def check_zse(request):
    zse_data, sale_date = get_zse_data()
    print('ZSE Sale Date =>', sale_date)
    json_data = json.dumps(zse_data)
    save_data = False
    zse_obj = ZSEData.objects.filter(trading_date=sale_date).first()
    print(zse_obj)
    if zse_obj:
        if zse_obj.data != json_data:
            save_data = True
            zse_obj.data_changed = True
            zse_obj.save()
    else:
        save_data = True
    if save_data:
        rec = ZSEData(data=json_data, trading_date=sale_date)
        rec.save()

    return render(request, 'spider/checkzse.html', {'zse_data': zse_data, 'sale_date': sale_date})

# Create your views here.
