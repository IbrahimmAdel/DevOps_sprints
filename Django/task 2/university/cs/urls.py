from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('students/', views.students_view, name='students'),
    path('courses/', views.courses_view, name='courses'),
    ]

