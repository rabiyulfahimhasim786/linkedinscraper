from django.urls import path
from . import views
from .views import (SpellcheckListview)
urlpatterns = [
    path('', views.home, name='home'),
    path('spellcheck/', SpellcheckListview.as_view(), name='SpellcheckListview')
    # path('', ),
]