from django.shortcuts import render
from django.http import HttpResponse
from cs.models import Students, Courses
from .forms import StudentForm, CoursesForm
from .import views
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


def home_view(request):
    if request.method != 'POST':
        form = CoursesForm(None)
        return render(request, 'home.html', {'form': form})
    else:
        details = CoursesForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, 'home.html', {'form': details})


def home2_view(request):
    if request.method != 'POST':
        form = StudentForm(None)
        return render(request, 'home.html', {'form': form})
    else:
        details = StudentForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse("data submitted successfully")
        else:
            return render(request, 'home2.html', {'form': details})
