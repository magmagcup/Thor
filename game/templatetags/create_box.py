from django import template

register = template.Library()

@register.filter
def create_box(value):
    # while '_' in value:
    start_ans = value.find('_')
    end_ans = value.find('_', start_ans+1)
    return value.replace(value[start_ans:end_ans+1], '<input type="text"></input>')
    # return value