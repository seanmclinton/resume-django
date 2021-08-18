from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import datetime

from .models import *


class ResumeViewTestCase(APITestCase):
    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Resume.objects.create(job_title="Test Job A", company="Test Company A", description="Test Description A",
                              start_date=job_a_start_date, end_date=job_a_end_date)

    def test_resume_url(self):
        url = reverse('resume/')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))