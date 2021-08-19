from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import exceptions
from django.forms.models import model_to_dict
from rest_framework import status
import json
from datetime import datetime
from .serializers import *
from .models import *
# Create your views here.


@csrf_exempt
def resume_list(request):
    if request.method == "GET":
        resumes = Resume.objects.all().order_by("-start_date")
        serializer = ResumeSerializer(resumes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        request_body = json.loads(request.body)
        response = {'created': []}
        try:
            for record in request_body['records']:
                resource_start_date = datetime.strptime(record['start_date'], '%m/%d/%Y')
                resource_end_date = datetime.strptime(record['end_date'], '%m/%d/%Y')
                new_object = Resume.objects.create(job_title=record['job_title'],
                                                   company=record['company'],
                                                   description=record['description'],
                                                   start_date=resource_start_date,
                                                   end_date=resource_end_date)
                response['created'].append(model_to_dict(new_object))
        except KeyError:
            # not sure about this one. let user know some objects were created but failed ?
            return JsonResponse(response, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # or just return an unhelpful 500?
            # return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse(response, safe=False, status=status.HTTP_201_CREATED)


@csrf_exempt
def resume_detail(request, pk):
    if request.method == "GET":
        try:
            resumes = Resume.objects.get(id=pk)
            serializer = ResumeSerializer(resumes, many=False)
            return JsonResponse(serializer.data, safe=False)
        except exceptions.ObjectDoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def contact_list(request):
    if request.method == "GET":
        contacts = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def contact_detail(request, pk):
    if request.method == "GET":
        try:
            contact = ContactInfo.objects.get(id=pk)
            serializer = ContactInfoSerializer(contact, many=False)
            return JsonResponse(serializer.data, safe=False)
        except exceptions.ObjectDoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return HttpResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def techology_used_list(request):
    if request.method == "GET":
        tech = TechnologyUsed.objects.all()
        serializer = TechnologyUsedSerializer(tech, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def technology_used_detail(request, pk):
    if request.method == "GET":
        try:
            tech_used = TechnologyUsed.objects.get(id=pk)
            serializer = TechnologyUsedSerializer(tech_used, many=False)
            return JsonResponse(serializer.data, safe=False)
        except exceptions.ObjectDoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)