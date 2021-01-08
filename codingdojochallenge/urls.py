from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.addShow, name='addShow'),
    # path('add-new-show/', views.addNewShow, name='addNewShow'),
    path('<int:show_id>', views.viewShow, name='viewShow')
]