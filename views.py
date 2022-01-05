from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('hi bro hello')

def welcome(request):
    return render(request,'index.html')

