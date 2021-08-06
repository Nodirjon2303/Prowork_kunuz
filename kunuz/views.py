from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def main(request):
    news = New.objects.all()
    context = {
        "news" : news
    }
    return render(request, 'index.html', context)