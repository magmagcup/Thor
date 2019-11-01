from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'game'

urlpatterns = [
    path('logout/', views.views_logout, name='logout'),
    path('', views.home_page, name='index'),
    path('home/', views.home_page, name='home'),
]
