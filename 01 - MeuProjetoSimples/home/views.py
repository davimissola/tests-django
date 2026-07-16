from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def saiba_mais(request):
    return render(request, 'home/saibamais.html')


def viagens_baratas(request):
    return render(request, 'home/viagensbaratas.html')
