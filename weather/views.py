from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from . import config


def current_weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=de3eb0b64c75657b96f68709f813d718'
    city = request.ipinfo.city
    
    return HttpResponse(json.dumps(request.ipinfo))