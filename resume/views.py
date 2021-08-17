from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .serializers import ResumeSerializer, ContactInfoSerializer
from rest_framework import viewsets
from .models import Resume, ContactInfo


# Create your views here.


class ResumeView(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()


class ContactInfoView(viewsets.ModelViewSet):
    serializer_class = ContactInfoSerializer
    queryset = ContactInfo.objects.all()


def get_personal_info(request):
    my_info = PersonalInfo.objects.first()
    data = {'first_name': my_info.first_name,
            'last_name': my_info.last_name,
            'city': my_info.city,
            'email': my_info.email,
            'linked_in_link': my_info.linked_in_link,
            'bio': my_info.bio}
    return JsonResponse(data)


def get_resume_items(request):
    resume_items = list(Resume.objects.all().order_by('-start_date').values())
    return JsonResponse({'data': resume_items})
