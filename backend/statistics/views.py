from rest_framework import generics
from .models import UsageStats
from .serializers import UsageStatsSerializer
from rest_framework.permissions import IsAdminUser

class UsageStatsListView(generics.ListAPIView):
    queryset = UsageStats.objects.all()
    serializer_class = UsageStatsSerializer
    permission_classes = [IsAdminUser]

