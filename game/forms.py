from django import forms
from django.utils.safestring import mark_safe
from game.models import Answer, Topic, Question

select_difficulty = [
    ('easy','Easy'),
    ('normal','Normal'),
    ('hard','Hard'),
    ('extreme','Extreme'),
]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'difficulty':forms.Select(
        choices=select_difficulty,
        ),
            'question_title': forms.Textarea(
        attrs={
            'id': 'title',
            'style' : 'height: 50px; font-size: 22px',
            'class' : 'mt-5',
            }
            ),
        'question_text':forms.Textarea(
        attrs={
            'id': 'question',
            'style' : 'height: 400px; font-size: 22px',
            'class' : 'mt-5',
            }
        )
        }
    # topic = forms.CharField(label='Topic', 
    # widget=forms.Select(
    #     choices=select_topic,
    #     )
    # )
    # difficulty = forms.CharField(label='Difficulty', 
    # widget=forms.Select(
    #     choices=select_difficulty,
    #     )
    # )
    # title = forms.CharField(label=mark_safe("Title</br>"), 
    # max_length=100000,
    # widget=
    # )
    # question = forms.CharField(label=mark_safe('Question</br>'), 
    # max_length=100000,
    # widget=forms.Textarea(
    #     attrs={
    #         'id': 'question',
    #         'style' : 'height: 400px; font-size: 22px',
    #         'class' : 'mt-5',
    #         }
    #     )
    # )

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
                'style': 'height: 28px; font-size: 16px; ',
                'size': box_length,
                'maxlength': ans_length,
                'title': hint,
                'onblur': 'checkAnswer()',
            })
