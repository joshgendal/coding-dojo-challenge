from django.shortcuts import render
from django.http import HttpResponse
from codingdojochallenge.forms import ShowForm

def addShow(request):
    context = {}
    context['form'] = ShowForm
    return render(request, 'codingdojochallenge/add-show.html', context=context)

def addNewShow(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # network = request.POST.get('network')
        # date = request.POST.get('date')
        # description = request.POST.get('description')
        form = ShowForm(request.POST)
        if form.is_valid():
            show_obj = form.save()
            # show_obj.save()
        # print(title, network, date, description)
    return HttpResponse('did it work?s')