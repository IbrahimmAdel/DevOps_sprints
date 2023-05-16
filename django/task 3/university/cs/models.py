from django.db import models


class Students (models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    semester = models.IntegerField()
    grade = models.CharField(max_length=20)


class Courses (models.Model):
    name = models.CharField(max_length=15)
    code = models.IntegerField()

