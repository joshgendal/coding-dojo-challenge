from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.addShow, name='index')
]