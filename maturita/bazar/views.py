from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
def index(request):

    return render(request, template_name='index.html')

class AutoListView(ListView):
    model = Auto
    context_object_name = 'auto_list'
    template_name = 'list.html'

class AutoDetailView(DetailView):
    model = Auto
    context_object_name = 'auto'
    template_name = 'detail.html'
