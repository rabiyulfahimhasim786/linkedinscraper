from django.urls import path
from . import views

from .views import (barcodelistview, barcodedeleteview, barcodeapiView, barcodefilelistview, barcodefiledeleteview, barcodefileapiView)

urlpatterns = [
    path('', views.index, name='index'),
    path('barcodedata/', barcodelistview.as_view(), name='barcodelistview'),
    path('barcode-generator/<int:pk>/', barcodedeleteview.as_view(), name='barcodedeleteview'),
    path('barcode-generator/', barcodeapiView.as_view(), name='barcodeapiView'),

    path('barcodedatafile/', barcodefilelistview.as_view(), name='barcodefilelistview'),
    path('barcode-creator/<int:pk>/', barcodefiledeleteview.as_view(), name='barcodefiledeleteview'),
    path('barcode-creator/', barcodefileapiView.as_view(), name='barcodefileapiView'),
]