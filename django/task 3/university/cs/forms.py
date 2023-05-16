from django import forms
from .models import Students, Courses
from django.forms import ModelForm


class StudentForm(ModelForm):
    class Meta:
        model = Students
        ﬁelds = ["f_name", "l_name", "semester", "grade"]

    def clean(self):
        super(StudentForm, self).clean()
        f_name = self.cleaned_data.get('f_name')
        l_name = self.cleaned_data.get('l_name')
        semester = self.cleaned_data.get('semester')
        grade = self.cleaned_data.get('grade')
        if len(f_name) < 2:
            self._errors['f_name'] = self.error_class([
                'Minimum 2 character1 required'])
        if len(l_name) < 2:
            self._errors['l_name'] = self.error_class([
                'Post Should Contain a minimum of 2 characters'])
        if semester < 0:
            self._errors['semester'] = self.error_class([
                'Post Should Contain a minimum of 0 integer'])
        if len(grade) < 1:
            self._errors['grade'] = self.error_class([
                'Post Should Contain a minimum of 1 characters'])
        return self.cleaned_data


class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        ﬁelds = ["name", "code"]

    def clean(self):
        super(CoursesForm, self).clean()
        name = self.cleaned_data.get('name')
        code = self.cleaned_data.get('code')

        if len(name) < 1:
            self._errors['name'] = self.error_class([
                'Minimum 1 characters required'])
        if code < 1:
            self._errors['code'] = self.error_class([
                'Minimum 1 integer required'])
        return self.cleaned_data
