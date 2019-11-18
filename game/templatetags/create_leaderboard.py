from django import template

register = template.Library()

@register.filter
def create_leaderboard(value):
    return 0