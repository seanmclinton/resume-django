from rest_framework import serializers
from .models import Resume, ContactInfo


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'job_title', 'company', 'description')


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('first_name', 'last_name', 'city', 'email', 'linked_in_link', 'bio')