from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.ProjectListView.as_view(), name='portfolio'),
    path('contact/', views.contact, name='contact'),
]