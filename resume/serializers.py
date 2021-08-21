from rest_framework import serializers
from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class TechnologyUsedSerializer(serializers.ModelSerializer):
    used_at = ResumeSerializer(read_only=True)

    class Meta:
        model = TechnologyUsed
        fields = "__all__"
