from .models import ZSEData
from rest_framework import serializers


class ZSEDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZSEData
        fields = ['data', 'trading_date', 'created', 'exported', 'data_changed']


