from django.urls import path
from django.conf.urls import url, include


from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home_page, name='index'),
    path('logout/', views.views_logout, name='logout'),
    path('form/',views.form_page, name="form"),
    path('home/', views.home_page, name='home'),
    path('<int:question_id>' , views.discard_form, name='discard'),
    path('preview',views.preview_form, name='preview'),
    path('stat/', views.get_stat, name='stat'),
    path('statistic/',views.statistic_page, name='statistic'),
    path('howtoplay/', views.how_to_play_page, name='howtoplay'),                 
    path('topic/', views.topic_page, name='topic'),
    path('<int:topic_id>/', views.question_page, name='question'),
    path('receive/<int:topic_id>/', views.receive_score, name='receive'),
    path('<int:question_id>/edit/', views.edit_form, name='edit'),
]
  