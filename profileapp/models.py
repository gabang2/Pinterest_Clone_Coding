from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # on_delete는 User가 없어졌을 때, 그와 관련된 Profile은 어떻게 할 것인지(같이 삭제)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # media 경로 밑에 profile이라는 경로 내에 이미지가 저장이 된다.
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
