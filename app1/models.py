from django.db import models

# Create your models here.

class Events(models.Model):
    description = models.TextField(null=True, max_length=1000)
    link = models.URLField(null=True)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description

class Gist(models.Model):
    email = models.EmailField(max_length=200, null=True, default='Annonymous Email')
    name = models.CharField(max_length=200, default='Annonymous', null=True)
    department = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=100, null=True)
    opinion = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)