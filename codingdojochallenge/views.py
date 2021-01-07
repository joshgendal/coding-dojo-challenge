from django.shortcuts import render
from django.http import HttpResponse

def addShow(request):
    return render(request, 'codingdojochallenge/add-show.html')

