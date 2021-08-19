from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase
import datetime

from .models import *


class ResumeViewTestCases(APITestCase):
    urlpatterns = [
        path('', include('resume.urls')),
    ]

    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Resume.objects.create(job_title="Test Job A", company="Test Company A", description="Test Description A",
                              start_date=job_a_start_date, end_date=job_a_end_date)

    def test_resume_list_url(self):
        url = reverse('resume_list')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
        # confirm data is returned accurately

    def test_resume_list_post(self):
        # test post list of resume items

        pass


class ContactInfoViewTestCases(APITestCase):
    urlpatterns = [
        path('', include('resume.urls')),
    ]

    def setUp(self) -> None:
        ContactInfo.objects.create(first_name="TestFirstName",
                                   last_name="TestLastName",
                                   city="TestCity",
                                   email="test@test.com",
                                   linked_in_link="testlink.com",
                                   bio="test_bio")

    def test_contact_list_url(self):
        url = reverse('contact_list')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))