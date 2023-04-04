from django.contrib import admin

from .models import Lesson, Weekday

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'teacher', 'place' )
    list_filter = ('type', 'name' )


@admin.register(Weekday)
class WeekdayAdmin(admin.ModelAdmin):
    list_display = ('name', 'parity', 'first_lesson', 'second_lesson',
                    'third_lesson', 'fourth_lesson', 'fifth_lesson')
    list_filter = ('parity', 'name')