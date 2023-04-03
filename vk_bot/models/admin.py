from django.contrib import admin

from .models import Lesson, Weekday

admin.site.register(Lesson)
admin.site.register(Weekday)