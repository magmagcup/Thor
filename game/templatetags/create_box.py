from django import template

register = template.Library()

@register.filter
def create_box(value):
    last_box_mark = 0
    answer_no = 1
    while (']]' in value):
        start = value.find('[[', last_box_mark)
        mid = value.find('|', last_box_mark)
        end = value.find(']]', last_box_mark)
        ans_length = mid - start
        replacement = f'<input type="text" size="{ans_length}" name="answer{answer_no}"></input>'
        value = value[:start] + replacement + value[end+2:]
        temp = last_box_mark
        last_box_mark = end + 1
        answer_no += 1
    return value
