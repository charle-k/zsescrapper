from django.contrib import admin

from .models import ZSEData


@admin.register(ZSEData)
class ZSEDataAdmin(admin.ModelAdmin):
    # date_hierarchy = 'trading_date'
    list_display = ('trading_date', 'created', 'data_changed')
    readonly_fields = ('trading_date',  'created', 'data_changed', 'data', )
