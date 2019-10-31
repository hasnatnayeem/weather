from django.urls import path
from . import views

urlpatterns = [
    path('weather/current', views.current_weather)
]
