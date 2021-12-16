from django.http import HttpResponse
from django.shortcuts import render
from myPortfolio.models import *
from django.db.models import Q

# Create your views here.

def home_view(request):
    title = request.GET.get("title")
    subtitle = request.GET.get('subtitle')
    content = request.GET.get('content')
    gitHub_link = request.GET.get('gitHub_link')
    link = request.GET.get('link')
    projectType = request.GET.get('link')
    
    projects = Projectos.objects.all()
    if title is not None:
        projects = projects.filter(title__id=title)
    if subtitle is not None:
        projects = projects.filter(subtitle__id=subtitle)
    if content is not None:
        projects = projects.filter(content__id=content)
    
    if gitHub_link is not None:
        projects = projects.filter(gitHub_link__id=gitHub_link)
    
    if link is not None:
        projects = projects.filter(link__id=link)
    
    if projectType is not None:
        projects = projects.filter(projectType__id=projectType)
    context = {
        'projects': projects
    }
    
    return render(request, template_name='home.html', context=context, status=200)


def list_projects(request, id=None):
    pass