from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    # image = models.ImageField()
    website = models.CharField(max_length=100)
    github = models.CharField(max_length=100)

    def __str__(self):
        return self.title
