from django.urls import path
from .views import UsageStatsListView

urlpatterns = [
    path('', UsageStatsListView.as_view(), name='usage-stats'),
]
