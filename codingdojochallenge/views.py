from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
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
    errors = []
    context['form'] = ShowForm
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            network = form.cleaned_data['network']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            # VALIDATE FORM ACCORDING TO SPECS
            if not title or not network or not date or not description:
                errors.append('Title must be at least 2 characters long!')
                context['errors'] = errors
            if len(title) < 2:
                errors.append('Title must be at least 2 characters long!')
            if len(network) < 3:
                errors.append('Network must be at least 3 characters long!')
            if len(description) < 10:
                errors.append('Description must be at least 10 characters long!')
            if errors:
                context['errors'] = errors
                return render(request, 'codingdojochallenge/add-show.html', context=context)
            # If fields pass validation, save to db and route to view show page
            s = Shows(title=title, network=network, release_date=date, description=description)
            s.save()
            
            return HttpResponseRedirect(f'/shows/{s.id}')
        else: 
            messages.error('invalid form')
            context['messages'] = messages
        # !!TODO: add else clause(s) for sad paths
    return render(request, 'codingdojochallenge/add-show.html', context=context)

def viewShow(request, show_id):
    q = Shows.objects.get(id=show_id)
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
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            q = Shows.objects.get(id=show_id)
            # pack vars from the edit form
            title = form.cleaned_data['title']
            network = form.cleaned_data['network']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            # set new values for queried show and save
            q.title = title
            q.network = network
            q.date = date
            q.description = description
            q.save()
            # Send user to view show page
            return HttpResponseRedirect(f'/shows/{show_id}')
    else:
        q = Shows.objects.get(id=show_id)
        form = ShowForm(initial={
            'title': q.title,
            'show_id': q.id,
            'date': q.release_date,
            'network': q.network,
            'description': q.description
        })
        context = {}
        context['form'] = form
        context['show_id'] = show_id
        return render(request, 'codingdojochallenge/edit-show.html', context=context)