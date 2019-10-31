from django.shortcuts import render
from django.http import HttpResponse

def current_weather(request):
    return HttpResponse("works")