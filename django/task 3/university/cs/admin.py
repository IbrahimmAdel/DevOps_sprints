from django.contrib import admin
from .models import Students, Courses


class StudentsAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "semester", "grade",)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)


admin.site.register(Students, StudentsAdmin)
admin.site.register(Courses, CoursesAdmin)

