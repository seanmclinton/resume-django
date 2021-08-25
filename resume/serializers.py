from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class TechnologyUsedSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnologyUsed
        fields = "__all__"
