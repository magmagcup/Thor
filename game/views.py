from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, 'game/login.html')


def page404(request, exception):
    return render(request, 'game/404.html')
