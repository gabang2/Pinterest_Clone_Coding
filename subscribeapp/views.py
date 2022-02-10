from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # subscribe.html페이지에서 project_pk라는 값으로 get인자를 보낼 때, kwargs에 pk라는 값으로 저장하여 projectapp:detail의 pk값으로 들어가게 됨.
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # project_pk를 가진 project를 찾을건데 만약 없다면 404예외처리를 함.
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # 이제 project와 user정보를 찾았으니 subscription을 해줄 것임.
        subscription = Subscription.objects.filter(user=user, project=project)

        # 있으면 없애기, 없으면 존재하게 만들기
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)
