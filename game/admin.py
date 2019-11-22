from django.contrib import admin
from .models import Question, Statistic

# Register your models here.

admin.site.register(Question)
admin.site.register(Statistic)