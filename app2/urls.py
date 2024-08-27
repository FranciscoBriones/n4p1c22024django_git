from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('saludo/', views.saludo)
]