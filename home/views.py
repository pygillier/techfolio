from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Contact


class IndexView(TemplateView):
    template_name = "home/index.html"


class AboutView(TemplateView):
    template_name = "home/about.html"


class ContactView(CreateView):
    model = Contact
    template_name = "home/contact.html"
    success_url = '/contact/success'

    fields = ['from_name', 'from_email', 'subject', 'content']


class ContactSuccessView(TemplateView):
    template_name = "home/success.html"
