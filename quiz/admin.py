from django.contrib import admin
import nested_admin
from .models import (
    Category,
    Quiz,
    Question,
    Option
)
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Option)

# Register your models here.
