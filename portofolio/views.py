from urllib import response
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, View
import json
from .models import Project
from .forms import CommentForm

# def home(request):
#     latest_projects = Project.objects.all().order_by("-date")[:3]
#     return render(request, "portofolio/home.html", {'latest_projects': latest_projects})

class HomeView(ListView):
    # template_name = "portofolio/home.html"
    template_name = "portofolio/homes.html"
    model = Project
    # order_by = ['-date']
    context_object_name = "latest_projects"

    def get_queryset(self):
        queryset = Project.objects.all().order_by("-date")
        data = queryset[:3]
        return data

# def projects_list(request):
#     projects = Project.objects.all().order_by("-date")
#     return render(request, "portofolio/projects-list.html", {'projects': projects})


class ProjectsListView(ListView):
    template_name = "portofolio/projects-list.html"
    model = Project
    order_by = ['-date']
    context_object_name = "projects"


# def project_details(request, slug):
#     context = {}
#     project = get_object_or_404(Project, slug=slug)   
#     context['project'] = project
#     context['tags'] = project.tags.all()
#     return render(request, "portofolio/project-details.html", context)

# class ProjectDetailView(DetailView):
#     template_name = "portofolio/project-details.html"
#     model = Project

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tags'] = self.object.tags.all()
#         context['quotes'] = self.object.quote_set.all()
#         context['add_comment_form'] = CommentForm()
#         return context


class ProjectDetailView(View):

    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        context = {
            "project": project,
            "tags": project.tags.all(),
            "add_comment_form": CommentForm(),
        }
        return render(request, "portofolio/project-details.html", context)

    def post(self, request, slug):
        project = Project.objects.get(slug=slug)
        add_comment_form = CommentForm(response.POST)

        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.project = project
            comment.save()
            return HttpResponseRedirect(reverse('project-detail-page', args=[slug]))

        context = {
            "project": project,
            "tags": project.tags.all(),
            "add_comment_form": add_comment_form,
        }
        return render(request, "portofolio/project-details.html", context)