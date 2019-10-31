from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from . import config



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def current_weather(request):
    print(get_client_ip(request))

    url = config.API['base_url'] + '/weather?q={}&units=metric&appid=' + config.API['key']
    city = request.ipinfo.city
    city_weather = requests.get(url.format(city)).json() 

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : 'http://openweathermap.org/img/w/{}.png'.format((city_weather['weather'][0]['icon']))
    }
    return HttpResponse(json.dumps(weather))


def forecast(request):
    url = config.API['base_url'] + '/forecast?q={}&cnt=50&units=metric&appid=' + config.API['key']
    city = request.ipinfo.city
    results = requests.get(url.format(city)).json() 

    midday = '12:00:00'
    filtered_results = []
    for weather in results['list']:
        date, time = weather['dt_txt'].split()
        if time == midday:
            data = {
                'city': results['city']['name'],
                'city_id': results['city']['id'],
                'date': date,
                'time': time,
                'temperature': weather['main']['temp'],
                'description': weather['weather'][0]['description'],
                'icon' : 'http://openweathermap.org/img/w/{}.png'.format((weather['weather'][0]['icon']))
            }
            filtered_results += [data]
    return HttpResponse(json.dumps(filtered_results))


def weather_in_capitals(request):
    url = config.API['base_url'] + '/group?id={}&units=metric&units=metric&appid=' + config.API['key']
    city_ids = config.API['captial_ids']
    results = requests.get(url.format(city_ids)).json()

    filtered_results = []
    for result in results['list']:
        weather = {
            'city' : result['name'],
            'temperature' : result['main']['temp'],
            'description' : result['weather'][0]['description'],
            'icon' : 'http://openweathermap.org/img/w/{}.png'.format((result['weather'][0]['icon']))
        }

        filtered_results += [weather]
    return HttpResponse(json.dumps(filtered_results))