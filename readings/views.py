from django.views.generic import ListView
from constance import config
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Link
import json


class IndexView(ListView):
    model = Link
    template_name = 'readings/index.html'


# IFTTT webhook
#

@csrf_exempt
@require_POST
def webhook(request):
    """
    IFTTT webhook, from https://medium.com/@raiderrobert/how-to-make-a-webhook-receiver-in-django-1ce260f4efff

    Requested format (with token from constance)
    {
      "title": "My beautiful title",
      "url": "https://myurl.com",
      "thumbnail_url":  "https://myurl.com/thumbnail.jpg",
      "excerpt": "This is a big excerpt",
      "tags": "tags1, tag2",
      "token": "anotsosecuretoken"
    }

    :param request:
    :return: HttpResponse
    """
    jsondata = request.body
    data = json.loads(jsondata)

    if 'token' in data and data['token'] == config.INCOMING_WH_TOKEN:
        data.pop('token')
        link = Link.objects.create(**data)
        link.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)
