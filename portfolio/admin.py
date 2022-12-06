"""Portfolio Admin"""
from django.contrib import admin
from .models import Project, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Project)

class ProjectAdmin(SummernoteModelAdmin):
    """Admin View for Project"""

    prepopulated_fields = {'slug': ['title']}

    list_display = ('title', 'slug', 'published', 'created_on')

    list_filter = ('published',)

    search_fields = ['title', 'content']

    summernote_fields = ('description')
