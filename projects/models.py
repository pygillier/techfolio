from django.db import models
from django_choice_object import Choice


class PlatformChoice(Choice):
    GITHUB = 1, "GitHub"
    GITLAB = 2, "GitLab",
    UNKNOWN = 10, "Unknown"


class Project(models.Model):

    name = models.CharField('Project name', max_length=255)
    repo_id = models.CharField('Project ID', max_length=255)
    url = models.URLField('Project URL')
    platform = models.IntegerField('Platform',
                                   choices=PlatformChoice,
                                   default=PlatformChoice.UNKNOWN)
    is_fork = models.BooleanField('This project is a fork', default=False)
    parent_url = models.URLField('When fork, parents URL',
                                 null=True,
                                 blank=True)
    is_visible = models.BooleanField('This project is visible', default=False)
    description = models.TextField()
    release_url = models.URLField('Releases URL')
    stars = models.IntegerField('Stars', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        platform = PlatformChoice.get_by_value(self.platform)
        return f"{platform}: {self.name}"

    class Meta:
        ordering = ['name', 'platform']
