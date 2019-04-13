from django.db import models


class Resume(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
