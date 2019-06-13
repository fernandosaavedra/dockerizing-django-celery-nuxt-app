from django.urls import path
from .views import DolarList

urlpatterns = [
    path('/', DolarList.as_view(), name='dolar'),
]