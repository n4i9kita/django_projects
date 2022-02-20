from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    tasks=task.objects.all() # how to know this is a model?
    # task.object.all(); now we can refer this in our tempalte

    context={'tasks':tasks}
    return render(request, 'task/list.html', context)
