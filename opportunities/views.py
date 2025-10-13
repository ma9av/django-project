from rest_framework import viewsets, permissions
from .models import Opportunity
from .serializers import OpportunitySerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Opportunity.objects.all()