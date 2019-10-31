from django.urls import path
from . import views

urlpatterns = [
    path('weather/current', views.current_weather),
    path('weather/forecast', views.forecast),
    path('weather/capitals', views.weather_in_capitals)
]
