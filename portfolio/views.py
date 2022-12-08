from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Project
from .forms import CommentForm

""" Views for the portfolio app"""

def index(request):
    """ Returns index.html """
    return render(request, 'index.html')

def about(request):
    """ Returns about.html """
    return render(request, 'about.html')

""" Class based view for the projects"""
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

""" Class based view for the project detail"""
class ProjectDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Project.objects.filter(published=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(published=True).order_by('-created_on')
        liked = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "project_detail.html",
            {
                "project": project,
                "comments": comments,
                "liked": liked
            },
        )


def contact(request):
    """ Returns contact.html """
    return render(request, 'contact.html')

