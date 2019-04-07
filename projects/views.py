from django.views.generic import TemplateView, ListView
from .models import Project


class IndexView(ListView):
    model = Project
    template_name = "projects/index.html"

    def get_queryset(self):
        return Project.objects.filter(is_visible=True)
