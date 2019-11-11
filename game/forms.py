from django import forms
from django.utils.safestring import mark_safe

class QuestionForm(forms.Form):
    title = forms.CharField(label=mark_safe("Title</br>"), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'title',
            'style' : 'height: 50px; font-size: 22px'
            }
        )
    )
    question = forms.CharField(label=mark_safe('Question</br>'), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'question',
            'style' : 'height: 400px; font-size: 22px'
            }
        )
    )
    answer = forms.CharField(label=mark_safe('Answer</br>'), 
    max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'answer',
            'style' : 'height: 50px; font-size: 22px'
            }
        )
    )
    hint = forms.CharField(label=mark_safe('Hint</br>'), max_length=100000,
    widget=forms.Textarea(
        attrs={
            'id': 'hint',
            'style' : 'height: 50px; font-size: 22px'
            }
        )
    )