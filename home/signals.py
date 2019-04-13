from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from django.core.mail import send_mail
from constance import config


@receiver(post_save, sender=Contact)
def my_handler(sender, instance, **kwargs):

    if kwargs['created'] is False:
        # Not a new contact, let's return
        return

    send_mail(
        subject=f'Nouveau contact: {instance.subject}',
        message=instance.content,
        from_email=config.EMAIL_DEFAULT_FROM,
        recipient_list=[config.EMAIL_DEFAULT_DEST],
        html_message=instance.content,
    )
