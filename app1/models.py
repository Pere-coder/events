from django.db import models

# Create your models here.

class Events(models.Model):
    description = models.TextField(null=True, max_length=1000)
    link = models.URLField(null=True)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description