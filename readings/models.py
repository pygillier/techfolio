from django.db import models


class Link(models.Model):

    title = models.CharField('Title', max_length=255)
    url = models.URLField('URL')
    thumbnail_url = models.URLField('Thumbnail URL')
    excerpt = models.TextField()

    tags = models.CharField('Tags', max_length=255)

    is_visible = models.BooleanField('Visible', default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
