from django import forms

class QuestionForm(forms.Form):
    title = forms.CharField(label='title', max_length=100000)
    question = forms.CharField(label='question', max_length=100000)
    answer = forms.CharField(label='answer', max_length=100000)
    hint = forms.CharField(label='hint', max_length=100000)