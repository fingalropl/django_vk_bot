from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import WeekdayViewSet, LessonViewSet


v1_router = DefaultRouter()

v1_router.register('weekday', WeekdayViewSet, basename='schedule')
v1_router.register('lesson', LessonViewSet, basename='schedule')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]