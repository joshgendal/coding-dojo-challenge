from django.shortcuts import render
from django.http import HttpResponse
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
            print('GETS AFTER SAVE', title, network, date, description, s.id)
            context = {
                'show': {
                'title': title,
                'network': network,
                'date': date,
                'description': description,
                'show_id': s.id
                }
            }

            return render(request, 'codingdojochallenge/view-show.html', context=context)
        # !!TODO: add else clause(s) for sad paths
    return render(request, 'codingdojochallenge/add-show.html', context=context)

# def addNewShow(request):
#     if request.method == 'POST':
#         form = ShowForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             network = form.cleaned_data['network']
#             date = form.cleaned_data['date']
#             description = form.cleaned_data['description']
#             s = Shows(title=title, network=network, release_date=date, description=description)
#             s.save()
#             print('GETS AFTER SAVE', title, network, date, description, s.id)
#             context = {
#                 'show': {
#                 'title': title,
#                 'network': network,
#                 'date': date,
#                 'description': description,
#                 'show_id': s.id
#                 }
#             }

#             return render(request, 'codingdojochallenge/view-show.html', context={
#                 'show_id':s.id
#             })
#         # !!TODO: add else clause(s) for sad paths
#     return HttpResponse('did it work?s')

def viewShow(request, show_id):
    q = Shows.objects.filter(id=show_id)
    print('query title: ', q.title)
    
