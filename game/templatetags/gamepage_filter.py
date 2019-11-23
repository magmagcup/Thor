from django import template
from game.forms import AnswerForm
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.filter(is_safe=True)
def create_box(value):
    answer_no = 0
    while (']]' in value):
        start = value.find('[[')
        mid = value.find('|')
        end = value.find(']]')
        ans_length = mid - start
        replacement = str(AnswerForm())
        value = value[:start] + replacement + value[end+2:]
        answer_no += 1
    return mark_safe(value)

@register.filter
def question(value, question_id):
    ans_queryset = value.filter(question_id=question_id)
    return [(a.answer_text) for a in ans_queryset]
