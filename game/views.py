from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    #redirect players to the homepage index
    return HttpResponseRedirect(reverse("game:index"))

def index_page(request):
    return render(request, 'game/login.html')

def page404(request, exception):
    return render(request, 'game/404.html')

def views_logout(request):
    logout(request)
    return redirect("game:index")

def home_page(request):
    return render(request, 'game/home.html')

