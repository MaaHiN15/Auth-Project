from django.shortcuts import render, HttpResponse

# Create your views here.

def index(req):
    return render(req, 'index.html', {})

def signin(req):
    return render(req, 'signin.html', {})