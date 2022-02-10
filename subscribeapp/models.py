from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # 이 두개가 한 쌍을 이루는 subscription은 unique하다(하나만 존재한다.)
        unique_together = ('user', 'project')