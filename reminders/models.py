from django.db import models
from contacts.models import Contact


class Remiders(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='reminders'
    )
    days_before = models.PositiveIntegerField()
    notifiy_at = models.TimeField(default='09:00')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
