from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    success_url = reverse_lazy('accountapp:hello_world')

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'


class ProjectListView(ListView, FormMixin):
    model = Project
    form_class = ProjectCreationForm
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 10
