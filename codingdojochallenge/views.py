from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from codingdojochallenge.forms import ShowForm
from codingdojochallenge.models import Shows


def index(request):
    # query db for all Shows
    shows = Shows.objects.all()
    context = {}
    context['shows'] = shows
    return render(request, 'codingdojochallenge/all-shows.html', context=context)

def addShow(request):
    context = {}
    context['form'] = ShowForm
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            network = form.cleaned_data['network']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            s = Shows(title=title, network=network, release_date=date, description=description)
            s.save()
            context = {
                'show': {
                'title': title,
                'network': network,
                'date': date,
                'description': description,
                'show_id': s.id
                }
            }
            return HttpResponseRedirect(f'/shows/{s.id}')
        # !!TODO: add else clause(s) for sad paths
    return render(request, 'codingdojochallenge/add-show.html', context=context)

def viewShow(request, show_id):
    q = Shows.objects.get(id=show_id)
    print('QUERY: ', q.title)
    context = {
        'show': {
            'title': q.title,
            'show_id': q.id,
            'date': q.release_date,
            'network': q.network,
            'description': q.description
        }
    }
    return render(request, 'codingdojochallenge/view-show.html', context=context)

def deleteShow(request, show_id):
    q = Shows.objects.filter(id=show_id).delete()
    return HttpResponseRedirect('/shows/')

def editShow(request, show_id):
    q = Shows.objects.get(id=show_id)
    form = ShowForm(initial={
        'title': q.title,
        'show_id': q.id,
        'date': q.release_date,
        'network': q.network,
        'description': q.description
    })
    # form = ShowForm(request.POST or None, instance = q)
    context = {}
    context['form'] = form
    context['show_id'] = show_id
    # context = {
    #     'show': {
    #     'title': q.title,
    #     'show_id': q.id,
    #     'date': q.release_date,
    #     'network': q.network,
    #     'description': q.description
    #     }
    # }
    return render(request, 'codingdojochallenge/edit-show.html', context=context)