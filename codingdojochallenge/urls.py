from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.addShow, name='addShow'),
    # path('add-new-show/', views.addNewShow, name='addNewShow'),
    path('<int:id>', views.viewShow, name='viewShow')
]