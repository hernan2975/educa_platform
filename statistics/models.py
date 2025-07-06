from django.db import models
from django.conf import settings
from contents.models import Course

class UsageStats(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    last_access = models.DateTimeField(auto_now=True)
    times_accessed = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
