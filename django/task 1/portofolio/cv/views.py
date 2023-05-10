from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def view(request):
    template = loader.get_template('temp.html')
    return HttpResponse(template.render())


