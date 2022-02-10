from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # content 필드가 만들어질 때 class랑 style을 미리 결정해준다고 생각(css라고 생각하기)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto; text-align:center'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
