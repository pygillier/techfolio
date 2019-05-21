from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):

    list_display = ('title', 'url', 'is_visible')
    list_filter = ('is_visible',)
