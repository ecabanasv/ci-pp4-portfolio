"""Forms for the portfolio app"""
from django import forms
from .models import Comment, Contact

class CommentForm(forms.ModelForm):
    """Form for the comments"""
    class Meta:
        """Meta class for the comments"""
        model = Comment
        fields = ('name', 'text_pros', 'text_cons', 'score',)

        labels = {
                    'name': 'Name',
                    'text_pros': 'Pros',
                    'text_cons': 'Cons',
                    'score': 'Score',
                }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'text_pros': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Pros'}),
            'text_cons': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Cons'}),
            'score': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
        }

class ContactForm(forms.ModelForm):
    """Form for the contact page"""
    class Meta:
        """Meta class for the contact page"""
        model = Contact
        fields = ('name', 'email', 'subject', 'message',)

        labels = {
                    'name': 'Name',
                    'email': 'Email',
                    'subject': 'Subject',
                    'message': 'Message',
                }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Message'}),
        }

