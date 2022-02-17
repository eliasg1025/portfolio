from django.shortcuts import render
from apps.projects.models import Experience, Project, Technology

def project_index(request):
    projects = Project.objects.all().prefetch_related('technologies')
    technologies = Technology.objects.order_by('-percentage')
    experiences = Experience.objects.order_by('-init_date')

    context = {
        'technologies': technologies,
        'projects': projects,
        'experiences': experiences,
    }

    return render(request, 'projects/project_index.html', context)
