from django.contrib import admin
from .models import Project


def publish(modeladmin, request, queryset):
    queryset.update(is_visible=True)


def unpublish(modeladmin, request, queryset):
    queryset.update(is_visible=False)


publish.short_description = "Publish selected projects"
unpublish.short_description = "Unpublish selected projects"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'platform', 'is_visible', 'is_fork')
    list_filter = ('platform', 'is_visible', 'is_fork')

    actions = [
        publish,
        unpublish
    ]