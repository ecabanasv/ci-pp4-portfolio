from django.contrib import admin
from .models import Project, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Project)

class ProjectAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
