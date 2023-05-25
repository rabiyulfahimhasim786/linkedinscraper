from django.urls import path
from . import views

from .views import (linkedinlistview, linkedindeleteview, LinkedinapiView)

urlpatterns = [
    path('', views.index, name='index'),
    path('linkedindata/', linkedinlistview.as_view(), name='linkedinlistview'),
    path('linkedindata/<int:pk>/', linkedindeleteview.as_view(), name='linkedindeleteview'),
    path('linkedin/', LinkedinapiView.as_view(), name='LinkedinapiView'),
]