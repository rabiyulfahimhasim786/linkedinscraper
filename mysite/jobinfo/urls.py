from django.urls import path
from . import views

from .views import (simplyhiredlistview, simplyhireddeleteview, simplyhiredapiView)

urlpatterns = [
    path('', views.index, name='index'),
    path('simplyhireddata/', simplyhiredlistview.as_view(), name='simplyhiredlistview'),
    path('simplyhireddata/<int:pk>/', simplyhireddeleteview.as_view(), name='simplyhireddeleteview'),
    path('simplyhired/', simplyhiredapiView.as_view(), name='simplyhiredapiView'),
]