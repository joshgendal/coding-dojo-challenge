from django.shortcuts import render
from django.http import HttpResponse

def addShow(request):
    return render(request, 'codingdojochallenge/add-show.html')

def addNewShow(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        network = request.POST.get('network')
        date = request.POST.get('date')
        description = request.POST.get('description')
        print(title, network, date, description)
    return HttpResponse(title)