from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=200, name=True)
    username = models.CharField(max_length=200, name=True)

    def __str__(self):
        return self.name
