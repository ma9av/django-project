from django.db import models

from leads.models import Lead

# Create your models here.
class Account(models.Model):
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)