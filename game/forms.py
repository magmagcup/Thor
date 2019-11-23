from django import forms
from django.utils.safestring import mark_safe
from game.models import Answer, Topic

object_topic = Topic.objects.all()
select_topic = [tuple([t.topic_name, t.topic_name]) for t in object_topic]
select_difficulty = [
    ('easy','Easy'),
    ('normal','Normal'),
    ('hard','Hard'),
    ('extreme','Extreme'),
]

class QuestionForm(forms.Form):
    topic = forms.CharField(label='Topic', 
    widget=forms.Select(
        choices=select_topic,
        )
    )
    difficulty = forms.CharField(label='Difficulty', 
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

class AnswerForm(forms.Form):
    answer = forms.CharField(
        label=mark_safe(''),
        max_length=1000,
        widget=forms.TextInput(
            attrs={
                'id': 'answer',
                'style': 'height: 50px; font-size: 22px; ',
                'onblur': 'checkAnswer()',
                'onmouseover': 'showHint()',
            }
        )
    )
