"""URLs for the portfolio app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/project_create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('portfolio/project_update/<slug:slug>/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('portfolio/project_delete/<slug:slug>/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('portfolio/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('portfolio/like/<slug:slug>', views.ProjectLikeView.as_view(), name='like_project'),
]
