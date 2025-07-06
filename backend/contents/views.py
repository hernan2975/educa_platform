from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Course
from .serializers import CourseSerializer
from users.permissions import IsPremiumUser

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_premium:
            return Course.objects.all()
        return Course.objects.filter(level_required='FREE')

    permission_classes = [IsAuthenticated]

