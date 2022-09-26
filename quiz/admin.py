from django.contrib import admin
import nested_admin
from .models import (
    Category,
    Quiz,
    Question,
    Option
)


class OptionAdmin(nested_admin.NestedTabularInline):
    model = Option
    extra = 5


class QuestionAdmin(nested_admin.NestedTabularInline):
    model = Question
    inlines = [OptionAdmin]
    extra = 5
    max_num = 20


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionAdmin]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)