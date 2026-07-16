from django.urls import path
from home.views import index, saiba_mais, viagens_baratas

urlpatterns = [
    path('', index, name='index'),
    path('saibamais/', saiba_mais, name='saiba_mais'),
    path('viagensbaratas/', viagens_baratas, name='viagens_baratas')
]