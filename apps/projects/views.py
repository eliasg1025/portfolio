from django.shortcuts import render
from apps.projects.models import Experience, Project, Technology

def project_index(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    experiences = Experience.objects.order_by('-init_date')

    context = {
        'technologies': technologies,
        'projects': projects,
        'experiences': experiences
    }

    return render(request, 'projects/project_index.html', context)
