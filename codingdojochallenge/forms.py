from django import forms
from codingdojochallenge.models import Shows

class ShowForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'title',
        'id': 'title-input'
    }))
    release_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'id': 'date-input',
        'name': 'date',
        'type': 'date'
    }))
    network = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'date-input',
        'name': 'date',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control description',
        'id': 'description-input',
        'name': 'description',
        'cols': '30',
        'rows': '5',
    }))


        # fields = ['title', 'release_date', 'network', 'description']