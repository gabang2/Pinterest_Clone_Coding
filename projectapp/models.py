from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, null=False)
    detail = models.TextField(null=False)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}:{self.title}'