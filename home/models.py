from django.db import models
from django_choice_object import Choice


class ContactStatus(Choice):
    RECEIVED = 1, "Received"
    REPLIED = 2, "Replied",
    WAITING = 3, "Waiting for anwser",
    CLOSED = 4, "Closed"


class Contact(models.Model):

    from_name = models.CharField('Sender name', max_length=255)
    from_email = models.EmailField('Sender address')
    subject = models.CharField('Subject', max_length=255)
    content = models.TextField("Message", blank=False, null=False)

    status = models.IntegerField('Status',
                                 choices=ContactStatus,
                                 default=ContactStatus.RECEIVED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ['-updated_at']
