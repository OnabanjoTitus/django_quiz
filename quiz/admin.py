from django.contrib import admin

# Register your models here.
from quiz.models import Question, Choice, Tweeter

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Tweeter)
