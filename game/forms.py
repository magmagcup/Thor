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
        attrs={
            'id': 'topic',
            'style' : 'height: 50px; font-size: 20x;',
            'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
        }
        )
    )
    difficulty = forms.CharField(label='Difficulty', 
    widget=forms.Select(
        choices=select_difficulty,
        attrs={
            'id': 'difficulty',
            'style' : 'height: 50px; font-size: 20px;',
            'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
            }
        )
    )
    title = forms.CharField(label=mark_safe("Title"), 
    max_length=100000,
    widget=forms.TextInput(
        attrs={
            'id': 'title',
            'style' : 'height: 50px; font-size: 20px',
            'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
            }
        )
    )
    question = forms.CharField(label=mark_safe('Question'), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'question',
            'style' : 'height: 750px; font-size: 18px; border-radius: 3%',
            'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
            }
        )
    )

class AnswerForm(forms.Form):
    answer = forms.CharField(label=mark_safe(''))

    def __init__(self, *args, **kwargs):
        ans_length = kwargs.pop('ans_length')
        box_length = kwargs.pop('box_length')
        hint = kwargs.pop('hint')
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'].widget = forms.TextInput(
            attrs={
                'id': 'answer',
                'style': 'height: 28px; font-size: 18px; ',
                'size': box_length,
                'maxlength': ans_length,
                'title': hint,
                'onblur': 'checkAnswer()',
            })
 