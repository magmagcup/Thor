from django.urls import path
from django.conf.urls import url


from . import views

app_name = 'game'

urlpatterns = [
    path('login/', views.index_page, name='login'),
]

