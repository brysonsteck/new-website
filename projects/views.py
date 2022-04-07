import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Project

# Create your views here.

def index(request):
  current_datetime = datetime.datetime.now()
  projects = Project.objects.all()
  return render(request, 'projects/index.html', {'current_datetime': current_datetime, 'projects': projects})

def project(request, project_name):
  current_datetime = datetime.datetime.now()
  try:
    project = Project.objects.get(title=project_name)
    project_img = project.image.url.split('/')[-1]
  except:
    return HttpResponseNotFound('<h1>Page not found</h1>')
  return render(request, 'projects/project.html', {'project': project, 'current_datetime': current_datetime, 'project_img': project_img})