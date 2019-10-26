from django.urls import path


from . import views

app_name = 'game'

urlpatterns = [
    path('login/', views.index_page, name='login'),
]

