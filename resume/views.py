from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .serializers import ResumeSerializer, ContactInfoSerializer
from .models import Resume, ContactInfo, TechnologyUsed
# Create your views here.


@csrf_exempt
def resume_list(request):
    if request.method == "GET":
        resumes = Resume.objects.all().order_by("-start_date")
        serializer = ResumeSerializer(resumes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        pass


@csrf_exempt
def resume_detail(request):
    pass

@csrf_exempt
def contact_list(request):
    if request.method == "GET":
        resumes = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(resumes, many=True)
        return JsonResponse(serializer.data, safe=False)