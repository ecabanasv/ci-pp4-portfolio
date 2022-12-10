"""Forms for the portfolio app"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Form for the comments"""
    class Meta:
        """Meta class for the comments"""
        model = Comment
        fields = ('name', 'text_pros', 'text_cons', 'score',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'text_pros': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Pros'}),
            'text_cons': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cons'}),
            'score': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Rate'}),
        }