from .models import Dolar
from .serializers import DolarSerializer
from rest_framework import generics


class DolarList(generics.ListCreateAPIView):
    queryset = Dolar.objects.filter(delta__isnull = False)
    serializer_class = DolarSerializer