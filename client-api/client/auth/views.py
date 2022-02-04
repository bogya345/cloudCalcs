from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_authenticated:
        redirect('/profile/')
    return HttpResponse("Hello, user, login pls")
