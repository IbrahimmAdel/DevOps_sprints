from django.shortcuts import render
from django.http import HttpResponse
from cs.models import Students, Courses


def welcome(request):
    return HttpResponse("welcome to university site")


def students_view(request):
    context = {}
    context["dataset"] = Students.objects.all()
    return render(request, "Students_view.html", context)


def courses_view(request):
    context = {}
    context["dataset"] = Courses.objects.all()
    return render(request, "Courses_view.html", context)
