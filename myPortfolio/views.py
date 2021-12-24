from django.http import HttpResponse
from django.shortcuts import redirect, render
from myPortfolio.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

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
    
    if len(projects) > 0:
        paginator = Paginator(projects, 6)
        page = request.GET.get('page')
        projects = paginator.get_page(page) 
    
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()   
    
    context = {
        'projects': projects,
        'parameters': parameters
    }
    
    return render(request, template_name='home.html', context=context, status=200)


def about(request):
    
    return render(request, template_name='about.html', status=200)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Fale comigo"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'corteisjunior@gmail.com', ['corteisjunior@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/")
        
    form = ContactForm()
    
    context = {
        'form': form
    }
    
    return render(request, template_name='contact.html', context=context,  status=200)
                            