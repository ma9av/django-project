from django.db import models

from accounts.models import Account
from leads.models import Lead

# Create your models here.
class Opportunity(models.Model):
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)