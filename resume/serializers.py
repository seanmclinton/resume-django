from rest_framework import serializers
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'job_title', 'company', 'description', 'start_date', 'end_date')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('first_name', 'last_name', 'city', 'email', 'linked_in_link', 'bio')


class TechnologyUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyUsed
        fields = ('tech_name', 'used_at')