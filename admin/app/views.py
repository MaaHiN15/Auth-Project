from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def index(req):
    return render(req, 'index.html', {})

def signin(req):
    return render(req, 'signin.html', {})

def signup(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        print(data)
        return JsonResponse({'status' : 200})

    return render(req, 'signup.html', {})