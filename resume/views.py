from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

from .serializers import ResumeSerializer, ContactInfoSerializer
from rest_framework import viewsets
from .models import Resume, ContactInfo, TechnologyUsed
# Create your views here.


@csrf_exempt
def resume_list(request):
    if request.method == "GET":
        resumes = Resume.objects.all().order_by("-start_date")
        serializer = ResumeSerializer(resumes, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def resume_detail(request):
    pass

@csrf_exempt
def contact_list(request):
    if request.method == "GET":
        resumes = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(resumes, many=True)
        return JsonResponse(serializer.data, safe=False)