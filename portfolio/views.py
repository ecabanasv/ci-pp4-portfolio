from django.shortcuts import render
from django.views import generic
from .models import Project

# Create your views here.

class ProjectListView(generic.ListView):
    """
    Class based view for the projects
    """
    model = Project
    template_name = 'portfolio.html'
    context_object_name = 'projects'

    def get_queryset(self):
        """
        Return the published projects
        """
        return Project.objects.filter(published=1).order_by('-created_on')
