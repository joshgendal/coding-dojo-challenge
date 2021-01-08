from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.addShow, name='addShow'),
    path('<int:show_id>', views.viewShow, name='viewShow'),
    path('<int:show_id>/destroy', views.deleteShow, name='deleteShow')
]