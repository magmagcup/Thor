from django import forms
from django.utils.safestring import mark_safe
from game.models import Answer, Topic

object_topic = Topic.objects.all()
select_topic = [tuple([t.topic_name,t.topic_name]) for t in object_topic]
select_difficulty = [
    ('easy','Easy'),
    ('normal','Normal'),
    ('hard','Hard'),
    ('extreme','Extreme'),
]

class QuestionForm(forms.Form):
    select_topic = forms.CharField(label='Topic', 
    widget=forms.Select(
        choices=select_topic,
        )
    )
    select_difficulty = forms.CharField(label='Difficulty', 
    widget=forms.Select(
        choices=select_difficulty,
        )
    )
    title = forms.CharField(label=mark_safe("Title</br>"), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'title',
            'style' : 'height: 50px; font-size: 22px',
            'class' : 'mt-5',
            }
        )
    )
    question = forms.CharField(label=mark_safe('Question</br>'), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'question',
            'style' : 'height: 400px; font-size: 22px',
            'class' : 'mt-5',
            }
        )
    )
