from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(project=project, user=user)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    template_name = 'subscribeapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        # values_list('project')를 통해서 user의 구독 프로젝트('project') 정보를 리스트로 저장(projects)에
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # Article모델에서 project속성이 projects리스트에 있는 것들만 article_list에 저장.
        article_list = Article.objects.filter(project__in=projects)
        return article_list
