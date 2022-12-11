"""Portfolio Admin"""
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Project, Comment


# Register your models here.


@admin.register(Project)

class ProjectAdmin(SummernoteModelAdmin):
    """Admin View for Project"""

    prepopulated_fields = {'slug': ['title']}

    list_display = ('title', 'slug', 'published', 'created_on')

    list_filter = ('published',)

    search_fields = ['title', 'content']

    summernote_fields = ('description')

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    """Admin View for Comment"""

    list_display = ('name', 'email', 'project', 'published', 'created_on')

    list_filter = ('published', 'created_on')

    search_fields = ('name', 'email', 'body')

    actions = ['publish_comment']

    def publish_comment(self, request, queryset):
        """Approve comments"""""
        queryset.update(published=True)
