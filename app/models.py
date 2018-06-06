from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    technologies_used = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    project_desription = models.TextField(null = True)

    def __str__(self):
        return self.title
