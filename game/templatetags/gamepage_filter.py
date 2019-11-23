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
        ans_length = mid - start - 2
        box_length = ans_length - 2
        if box_length < 1:
            box_length = 1
        replacement = str(AnswerForm(ans_length=ans_length, box_length=box_length))
        value = value[:start] + replacement + value[end+2:]
        answer_no += 1
    return mark_safe(value)

@register.filter(is_safe=True)
def get_answer(value, question_id):
    ans_queryset = value.filter(question_id=question_id)
    return mark_safe([ans.answer_text for ans in ans_queryset])

@register.filter
def get_hint(value, question_id):
    ans_queryset = value.filter(question_id=question_id)
    return mark_safe([ans.hint_text for ans in ans_queryset])
