from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request):
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {
        'boldmessage': 'Ken Leung'
    }
    return render(request, 'rango/about.html', context_dict)