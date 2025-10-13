from django.db import models

class LeadType(models.TextChoices):
    INDIVIDUAL = 'individual', 'Individual'
    CORPORATE = 'corporate', 'Corporate'


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    lead_type = models.CharField(max_length=255, choices=LeadType.choices)
    custom_fields = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
