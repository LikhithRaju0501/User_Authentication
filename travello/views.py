from django.shortcuts import render
from . models import Destination


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html' , {'dests' : dests})

def book(request):
    return render(request , 'book.html' , {})

def confirm(request):
    return render(request , 'confirm.html' , {})
