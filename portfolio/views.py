""" Portfolio views"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Project
from .forms import CommentForm, ContactForm, ProjectForm


def index(request):
    """Returns index.html"""
    return render(request, "index.html", {"title": "home"})


def about(request):
    """Returns about.html"""
    return render(request, "about.html", {"title": "about"})


class ProjectListView(generic.ListView):
    """
    Class based view for the projects
    """

    model = Project
    template_name = "portfolio.html"
    context_object_name = "projects"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        """
        Return the published projects
        """
        queryset = Project.objects.filter(published=1).order_by("-created_on")
        queryset_un = Project.objects.filter(published=0).count()
        if queryset_un > 0:
            unpublish_b = True
        else:
            unpublish_b = False
        return render(
            request,
            "portfolio.html",
            {"projects": queryset, "unpublish_b": unpublish_b},
        )


class UnpublishProjectListView(generic.ListView):
    """
    Class based view for the unpublished projects
    """

    model = Project
    template_name = "portfolio_unpublished.html"
    context_object_name = "projects"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        """
        Return the unpublished projects
        """
        queryset = Project.objects.filter(published=0).order_by("-created_on")
        queryset_pu = Project.objects.filter(published=1).count()
        if queryset_pu > 0:
            publish_b = True
        else:
            publish_b = False
        return render(
            request,
            "portfolio_unpublished.html",
            {"projects": queryset, "publish_b": publish_b},
        )


class ProjectDetailView(View):
    """Class based view for the project detail"""

    def get(self, request, slug, *args, **kwargs):
        """Get method for the project detail"""
        queryset = Project.objects.filter(published=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(published=True).order_by("-created_on")
        liked = False
        wait = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "project_detail.html",
            {
                "title": project.title,
                "project": project,
                "comments": comments,
                "liked": liked,
                "wait": wait,
                "form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Post method for the project detail"""
        queryset = Project.objects.filter(published=1)
        project = get_object_or_404(queryset, slug=slug)
        comments = project.comments.filter(published=True).order_by("-created_on")
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
            return HttpResponseRedirect(reverse("project_detail", args=[str(slug)]))

        return render(
            request,
            "project_detail.html",
            {
                "title": project.title,
                "project": project,
                "comments": comments,
                "liked": liked,
                "wait": wait,
                "form": form,
            },
        )


class ProjectLikeView(View):
    """Class based view for the project like"""

    def post(self, request, slug, *args, **kwargs):
        """get method for the project like"""
        project = get_object_or_404(Project, slug=slug)
        if project.likes.filter(id=self.request.user.id).exists():
            project.likes.remove(self.request.user)
        else:
            project.likes.add(self.request.user)

        return HttpResponseRedirect(reverse("project_detail", args=[str(slug)]))


class ProjectCreateView(generic.CreateView):
    """Class based view for the project create"""

    model = Project
    template_name = "project_create.html"
    form_class = ProjectForm
    success_url = "/portfolio/"

    def post(self, request, *args, **kwargs):
        """Post method for the project create"""
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect(
                reverse("project_detail", args=[str(form.instance.slug)])
            )

        return render(
            request,
            "project_create.html",
            {
                "title": "create project",
                "form": form,
            },
        )

    def form_valid(self, form):
        """Form validation for the project create"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(generic.UpdateView):
    """Class based view for the project update"""

    model = Project
    template_name = "project_update.html"
    form_class = ProjectForm
    success_url = "/portfolio/"


class ProjectDeleteView(generic.DeleteView):
    """Class based view for the project delete"""

    model = Project
    template_name = "project_delete.html"
    success_url = "/portfolio/"


class ContactView(View):
    """Class based view for the contact"""

    def get(self, request, *args, **kwargs):
        """Get method for the contact"""
        return render(
            request, "contact.html", {"form": ContactForm(), "title": "contact"}
        )

    def post(self, request, *args, **kwargs):
        """Post method for the contact"""
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail(
                    "Contact Form",
                    message,
                    "ecvoracle@gmail.com",
                    ["ecvoracle@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return HttpResponseRedirect(reverse("contact"))
        return render(request, "contact.html", {"form": form, "title": "contact"})
