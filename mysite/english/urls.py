from django.urls import path
from . import views
from .views import (SpellcheckListview, SpellcheckDeleteview )
urlpatterns = [
    path('', views.home, name='home'),
    path('spellcheck/', SpellcheckListview.as_view(), name='SpellcheckListview'),
    path('spellcheck/<int:pk>/', SpellcheckDeleteview.as_view(), name='SpellcheckDeleteview')
    # path('', ),
]