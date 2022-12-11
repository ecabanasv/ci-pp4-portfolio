"""Forms for the portfolio app"""
from django import forms
from .models import Comment, Contact, Project


class CommentForm(forms.ModelForm):
    """Form for the comments"""

    class Meta:
        """Meta class for the comments"""

        model = Comment
        fields = (
            "name",
            "text_pros",
            "text_cons",
            "score",
        )

        labels = {
            "name": "Name",
            "text_pros": "Pros",
            "text_cons": "Cons",
            "score": "Score",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "text_pros": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Pros"}
            ),
            "text_cons": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Cons"}
            ),
            "score": forms.Select(
                attrs={"class": "form-control", "placeholder": "Rate"}
            ),
        }


class ContactForm(forms.ModelForm):
    """Form for the contact page"""

    class Meta:
        """Meta class for the contact page"""

        model = Contact
        fields = (
            "name",
            "email",
            "subject",
            "message",
        )

        labels = {
            "name": "Name",
            "email": "Email",
            "subject": "Subject",
            "message": "Message",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Subject"}
            ),
            "message": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Message"}
            ),
        }


class ProjectForm(forms.ModelForm):
    """Form for the project page"""

    class Meta:
        """Meta class for the project page"""

        model = Project
        fields = (
            "title",
            "excerpt",
            "description",
            "image_main",
            "live_url",
            "github_url",
            "published",
        )

        labels = {
            "title": "Title",
            "slug": "Slug",
            "excerpt": "Excerpt",
            "description": "Description",
            "image_main": "Image",
            "live_url": "URL",
            "github_url": "Github",
            "published": "Published",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Slug"}
            ),
            "excerpt": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Excerpt"}
            ),
            "description": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Description"}
            ),
            "image_main": forms.FileInput(
                attrs={"class": "form-control", "placeholder": "Image"}
            ),
            "live_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Live URL"}
            ),
            "github_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Github"}
            ),
            "published": forms.RadioSelect(attrs={"class": "form-control"}),
        }
