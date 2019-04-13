from django import template
from django.utils.safestring import mark_safe
from ..models import PlatformChoice


register = template.Library()


@register.filter(name='platform_icon', is_safe=True)
def get_platform_icon(platform_id):
    if platform_id == PlatformChoice.GITHUB:
        icon = "github"
    elif platform_id == PlatformChoice.GITLAB:
        icon = "gitlab"
    else:
        icon = "question-circle"

    return mark_safe(f'<i class="fab fa-{icon}"></i>')
