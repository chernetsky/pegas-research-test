from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='data-home'),
    path('data/', views.data, name='data-connect')   
]
