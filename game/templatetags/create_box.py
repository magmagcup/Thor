from django import template

register = template.Library()

def string_check(value, first_char, last_char, marker, str_type):
    while (last_char in value):
        start = value.find(first_char, marker)
        end = value.find(last_char, start+1)
        length = end - start
        if str_type == 'answer':
            replacement = f'<input type="text" size="{length}"></input>'
        elif str_type == 'hint':
            replacement = ''
        value = value[:start] + replacement + value[end+1:]
        marker = end + 1
    return value

@register.filter
def create_box(value):
    last_box_mark, last_hint_mark = 0, 0
    value = string_check(value, '_', '_', last_box_mark, 'answer')
    value = string_check(value, '(', ')', last_hint_mark, 'hint')
    return value
