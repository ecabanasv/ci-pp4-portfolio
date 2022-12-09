""" Portfolio views"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Project
from .forms import CommentForm

def index(request):
    """ Returns index.html """
    return render(request, 'index.html')

def about(request):
    """ Returns about.html """
    return render(request, 'about.html')


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


class ProjectDetailView(View):
    """ Class based view for the project detail"""
    def get(self, request, slug, *args, **kwargs):
        """Get method for the project detail"""
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

    def post(self, request, slug, *args, **kwargs):
        """Post method for the project detail"""
        queryset = Project.objects.filter(published=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(published=True).order_by('-created_on')
        liked = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            return HttpResponseRedirect(reverse('project_detail', args=[str(slug)]))

        return render(
            request,
            "project_detail.html",
            {
                "project": project,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )


class ProjectLikeView(View):
    """ Class based view for the project like"""
    def post(self, request, slug, *args, **kwargs):
        """get method for the project like"""
        project = get_object_or_404(Project, slug=slug)
        if project.likes.filter(id=self.request.user.id).exists():
            project.likes.remove(self.request.user)
        else:
            project.likes.add(self.request.user)

        return HttpResponseRedirect(reverse('project_detail', args=[str(slug)]))


def contact(request):
    """ Returns contact.html """
    return render(request, 'contact.html')
