import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from django.conf import settings

from .utils import get_zse_data
from .models import ZSEData


def index(request):
    trading_date = timezone.now().date()
    zse_data = ZSEData.objects.filter(trading_date__lte=trading_date).first()
    counters = []
    if zse_data:
        trading_date = zse_data.trading_date
        counters = json.loads(zse_data.data)
    scrapping_key = settings.SCRAPPING_KEY
    return render(request, 'spider/index.html', {'zse_data': zse_data,
                                                 'trading_date': trading_date,
                                                 'counters': counters,
                                                 'scrapping_key': scrapping_key})


def check_zse(request):
    key = request.GET.get('key', '')
    if key == settings.SCRAPPING_KEY:
        zse_data, sale_date = get_zse_data()
        print('ZSE Sale Date =>', sale_date)
        json_data = json.dumps(zse_data)
        zse_obj = ZSEData.objects.filter(trading_date=sale_date).first()
        # print(zse_obj)
        if zse_obj:
            if zse_obj.data != json_data:
                zse_obj.data = json_data
                zse_obj.data_changed = True
                zse_obj.save()
        else:
            rec = ZSEData(data=json_data, trading_date=sale_date)
            rec.save()

        return render(request, 'spider/checkzse.html', {'zse_data': zse_data, 'sale_date': sale_date})
    else:
        # Key forwarded by browser agent does not match current scrapping key
        return HttpResponse('To be or not to be...')


def daily_pricesheet_listing(request):
    zse_data_list = ZSEData.objects.all()
    paginator = Paginator(zse_data_list, 20) # Show 20 dates per page.
    page_number = request.GET.get('page')
    pricesheet_list = paginator.get_page(page_number)
    return render(request, 'spider/daily_pricesheet_listing.html', {'pricesheet_list': pricesheet_list})


def daily_pricesheet(request, id):
    zse_data = get_object_or_404(ZSEData, id=id)
    trading_date = zse_data.trading_date
    counters = json.loads(zse_data.data)
    return render(request, 'spider/daily_pricesheet.html', {'zse_data': zse_data,
                                                 'trading_date': trading_date,
                                                 'counters': counters})