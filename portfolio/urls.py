from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.ProjectListView.as_view(), name='portfolio'),
]