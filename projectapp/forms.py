from django.forms import ModelForm

from profileapp.models import Profile
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'detail']
