from django import template
from django.utils.safestring import mark_safe
from game.forms import AnswerForm

register = template.Library()

@register.filter
def boxed(value):
    while ']]' in value:
        start = value.find('[[')
        mid = value.find('|')
        end = value.find(']]')
        ans_length = mid - start - 2
        box_length = ans_length
        if box_length < 1:
            box_length = 1
        hint = value[mid+1:end]
        replacement = str(AnswerForm(ans_length=ans_length,
                                     box_length=str(box_length)+"ch", hint=hint))
        value = value[:start] + replacement + value[end+2:]
    return mark_safe(value)
