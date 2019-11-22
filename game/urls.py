from django.urls import path
from django.conf.urls import url, include


from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('logout/', views.views_logout, name='logout'),
    path('form/',views.form_page, name="form"),
    path('home/', views.home_page, name='home'),
    path('set/' , views.get, name='set'),
    path('stat/', views.get_stat, name='stat'),
    path('statistic/',views.statistic_page, name='statistic'),
]