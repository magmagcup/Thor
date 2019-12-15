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
            'topic':forms.Select(
                attrs={
                'id': 'topic',
                'style' : 'height: 50px; font-size: 20px;',
                'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
                }
            ),
            'difficulty':forms.Select(
                choices=select_difficulty,
                attrs={
                    'id': 'difficulty',
                    'style' : 'height: 50px; font-size: 20px;',
                    'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
                }
            ),
            'question_title': forms.Textarea(
                attrs={
                    'id': 'title',
                    'style' : 'height: 50px; font-size: 18px; resize: none',
                    'class' : 'col-10 mt-2 p-3 d-flex justify-content-center',
                }
            ),
            'question_text':forms.Textarea(
                attrs={
                    'id': 'question',
                    'style' : 'height: 750px; font-size: 18px; border-radius: 3%',
                    'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
                }
            )
        }

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
                'style': 'height: 28px; font-size: 22px; ',
                'size': box_length,
                'maxlength': ans_length,
                'title': hint,
                'onblur': 'checkAnswer()',
            })

class AForm(forms.Form):
    c = forms.ChoiceField(choices=(("a","A"), ("b", "B")), disabled=True)
    