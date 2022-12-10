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
    paginate_by = 6

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
        wait = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "project_detail.html",
            {
                "project": project,
                "comments": comments,
                "liked": liked,
                "wait": wait,
                "form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Post method for the project detail"""
        queryset = Project.objects.filter(published=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(published=True).order_by('-created_on')
        liked = False
        wait = True
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user.username
            form = form.save(commit=False)
            form.project = project
            form.save()
            return HttpResponseRedirect(reverse('project_detail', args=[str(slug)]))

        return render(
            request,
            "project_detail.html",
            {
                "project": project,
                "comments": comments,
                "liked": liked,
                "wait": wait,
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

class ProjectCreateView(generic.CreateView):
    """ Class based view for the project create"""
    model = Project
    fields = ['title', 'excerpt', 'description', 'image_main', 'live_url', 'github_url', 'published']

class ProjectUpdateView(generic.UpdateView):
    """ Class based view for the project update"""
    model = Project
    fields = ['title', 'excerpt', 'description', 'image_main', 'live_url', 'github_url', 'published']

class ProjectDeleteView(generic.DeleteView):
    """ Class based view for the project delete"""
    model = Project
    success_url = '/portfolio/'


def contact(request):
    """ Returns contact.html """
    return render(request, 'contact.html')
