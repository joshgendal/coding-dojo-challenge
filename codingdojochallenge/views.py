from django.shortcuts import render
from django.http import HttpResponse
from codingdojochallenge.forms import ShowForm
from codingdojochallenge.models import Shows

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
            # show_obj = form.save()
            title = form.cleaned_data['title']
            network = form.cleaned_data['network']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            s = Shows(title=title, network=network, release_date=date, description=description)
            s.save()
            print('GETS AFTER SAVE', title, network, date, description)
            # show_obj.save()
        # print(title, network, date, description)
    return HttpResponse('did it work?s')