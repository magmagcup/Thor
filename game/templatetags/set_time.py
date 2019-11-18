from django import template

register = template.Library()

@register.filter
def set_interval(value):
    return 0