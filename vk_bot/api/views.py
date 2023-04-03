from rest_framework import viewsets
from models.models import Lesson, Weekday
from .serializers import WeekdaySerializers, LessonSerializers
from django_filters.rest_framework import DjangoFilterBackend

class WeekdayViewSet(viewsets.ModelViewSet):
    queryset = Weekday.objects.all()
    serializer_class = WeekdaySerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'parity') 



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializers
