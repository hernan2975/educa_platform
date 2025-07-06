from rest_framework import serializers
from .models import UsageStats

class UsageStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsageStats
        fields = '__all__'

