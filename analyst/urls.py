from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('main.html',views.main),
    path('years.html',views.years),
    path('cities.html',views.cities),
    path('static/assets/css/',views.css),
    path('static/assets/vendor/',views.vendor),
]
