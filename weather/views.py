from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from . import config


def current_weather(request):
    url = config.API['base_url'] + '/weather?q={}&units=metric&appid=' + config.API['key']
    city = "Dhaka"
    city_weather = requests.get(url.format(city)).json() 

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['main'],
        'icon' : 'http://openweathermap.org/img/w/{}.png'.format((city_weather['weather'][0]['icon']))
    }
    return HttpResponse(json.dumps(weather))