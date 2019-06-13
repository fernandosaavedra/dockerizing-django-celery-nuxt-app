from .models import Dolar
from rest_framework import serializers


class DolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dolar
        fields = ('date', 'val', 'delta')