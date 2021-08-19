from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import exceptions
from django.forms.models import model_to_dict
from rest_framework import status, generics
from rest_framework.decorators import api_view
import json
from datetime import datetime
from .serializers import *
from .models import *
# Create your views here.


class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all().order_by("-start_date")
    serializer_class = ResumeSerializer


class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all().order_by("-start_date")
    serializer_class = ResumeSerializer


class ContactInfoList(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContactInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class TechnologyUsedList(generics.ListCreateAPIView):
    queryset = TechnologyUsed.objects.all()
    serializer_class = TechnologyUsedSerializer


class TechnologyUsedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnologyUsed.objects.all()
    serializer_class = TechnologyUsedSerializer
