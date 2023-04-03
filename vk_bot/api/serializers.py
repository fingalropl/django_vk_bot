from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from models.models import Lesson, Weekday


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class WeekdaySerializers(serializers.ModelSerializer):
    first_lesson = SerializerMethodField(method_name='get_first_lesson')
    second_lesson = SerializerMethodField(method_name='get_second_lesson')
    third_lesson = SerializerMethodField(method_name='get_third_lesson')
    fourth_lesson = SerializerMethodField(method_name='get_fourth_lesson')
    fifth_lesson = SerializerMethodField(method_name='get_fifth_lesson')
    class Meta:
        model = Weekday
        fields = '__all__'
    
    def get_first_lesson(self, obj):
        first_lesson = Lesson.objects.filter(id=obj.first_lesson.id)
        return LessonSerializers(first_lesson, many = True).data
    
    def get_second_lesson(self, obj):
        first_lesson = Lesson.objects.filter(id=obj.second_lesson.id)
        return LessonSerializers(first_lesson, many = True).data
    
    def get_third_lesson(self, obj):
        first_lesson = Lesson.objects.filter(id=obj.third_lesson.id)
        return LessonSerializers(first_lesson, many = True).data
    
    def get_fourth_lesson(self, obj):
        first_lesson = Lesson.objects.filter(id=obj.fourth_lesson.id)
        return LessonSerializers(first_lesson, many = True).data
    
    def get_fifth_lesson(self, obj):
        first_lesson = Lesson.objects.filter(id=obj.fifth_lesson.id)
        return LessonSerializers(first_lesson, many = True).data