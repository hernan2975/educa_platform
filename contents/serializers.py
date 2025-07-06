from rest_framework import serializers
from .models import Course, Pictogram

class PictogramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictogram
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    pictograms = PictogramSerializer(many=True, read_only=True, source='pictogram_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'image', 'level_required', 'pictograms']
