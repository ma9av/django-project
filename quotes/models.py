from django.db import models

from opportunities.models import Opportunity

class Quote(models.Model):
    opportunity_id = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)