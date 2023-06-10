from django.urls import path
from . import views

app_name = 'portofolio'

urlpatterns = [
    # path("", views.home, name="home-page"),
    path("", views.HomeView.as_view(), name="home-page"),
    # path("projects", views.projects_list, name="projects-list-page"),
    path("projects", views.ProjectsListView.as_view(), name="projects-list-page"),
    # path("projects/<slug:slug>", views.project_details, name="project-detail-page"),
    path("projects/<slug:slug>", views.ProjectDetailView.as_view(), name="project-detail-page"),
]