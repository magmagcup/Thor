from django.urls import path


from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home_page, name='home'),
]

