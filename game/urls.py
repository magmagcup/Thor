from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'game'

urlpatterns = [
    path("", views.index_page, name="index"),
    path('login/', views.index_page, name='login'),
    path('logout/', views.views_logout, name='logout'),
]
