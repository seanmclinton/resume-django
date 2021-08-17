from rest_framework import serializers
from .models import Resume, PersonalInfo


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'job_title', 'company', 'description')


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = ('first_name', 'last_name', 'city')