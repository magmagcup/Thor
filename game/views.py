from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.


def index_page(request):
    return render(request, 'game/login.html')


def page404(request, exception):
    return render(request, 'game/404.html')

def views_logout(request):
    logout(request)
    return redirect("game:index")