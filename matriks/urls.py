from django.urls import path
from .views import CreateRCIView, RCIList, CreateReklamasiView, ReklamasiList, matriks
from django.contrib.auth import views

urlpatterns = [
    path('inputrci/', CreateRCIView.as_view(), name='input-rci'),
    path('listrci/', RCIList.as_view(), name='list-rci'),
    path('inputreklamasi/', CreateReklamasiView.as_view(), name='input-reklamasi'),
    path('listreklamasi/', ReklamasiList.as_view(), name='list-reklamasi'),
    path('matriks/', matriks, name='matriks')
]

