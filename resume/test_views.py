from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase
import datetime
import json

from .models import *


class JobViewTestCases(APITestCase):
    urlpatterns = [
        path('', include('resume.urls')),
    ]

    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Job.objects.create(job_title="Test Job A", company="Test Company A", description="Test Description A",
                              start_date=job_a_start_date, end_date=job_a_end_date)

        job_b_start_date = datetime.datetime(2019, 2, 4, 0, 0)
        job_b_end_date = datetime.datetime(2020, 2, 3, 0, 0)
        Job.objects.create(job_title="Test Job B", company="Test Company B", description="Test Description B",
                              start_date=job_b_start_date, end_date=job_b_end_date)

    def test_job_list_get(self) -> None:
        url = reverse('job_list')
        response = self.client.get(url)
        response_json = json.loads(response.content.decode())
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response_json, [{'id': 1,
                                          'job_title': 'Test Job A',
                                          'company': 'Test Company A',
                                          'description': 'Test Description A',
                                          'start_date': '2020-02-04',
                                          'end_date': '2021-01-05'},
                                         {
                                            'id': 2,
                                            'job_title': 'Test Job B',
                                            'company': 'Test Company B',
                                            'description': 'Test Description B',
                                            'start_date': '2019-02-04',
                                            'end_date': '2020-02-03'
                                         }])

    def test_resume_detail_get(self) -> None:
        pass

    def test_resume_list_get_ordering(self) -> None:
        # testing for resume items sorted in descending order by start date
        url = reverse('job_list')
        response = self.client.get(url)
        response_json = json.loads(response.content.decode())
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response_json[0]['start_date'], "2020-02-04")
        self.assertEqual(response_json[1]['start_date'], "2019-02-04")

        # confirm data is returned accurately

    def test_resume_post(self) -> None:
        # test post resume
        resume_to_post = {'job_title': 'Test Job C',
                          'company': 'Test Company C',
                          'description': 'Test Description C',
                          'start_date': '2005-09-06',
                          'end_date': '2006-10-04'}
        url = reverse('job_list')
        response = self.client.post(url, resume_to_post, format='json')
        response_json = json.loads(response.content.decode())
        resume_to_post['id'] = 3
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response_json, resume_to_post)

    def test_resume_poor_format_post(self) -> None:
        resume_to_post = {'job_asdf': 'Test Job C',
                          'company': 'Test Company C',
                          'description': 'Test Description C',
                          'start_date': '2005-09-06',
                          'end_date': '2006-10-04'}
        url = reverse('job_list')
        response = self.client.post(url, resume_to_post, format='json')
        response_json = json.loads(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_json, {"job_title": ["This field is required."]})


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

    def test_contact_list_get(self) -> None:
        url = reverse('contact_list')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))

    def test_contact_detail_get(self) -> None:
        pass

    def test_contact_post(self) -> None:
        pass

    def test_contact_poor_format_post(self) -> None:
        pass


class TechnologyUsedViewTestCases(APITestCase):
    urlpatterns = [
        path('', include('resume.urls')),
    ]

    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Job.objects.create(job_title="Test Job A",
                              company="Test Company A",
                              description="Test Description A",
                              start_date=job_a_start_date,
                              end_date=job_a_end_date)

        resume_object = Job.objects.get(job_title="Test Job A")
        TechnologyUsed.objects.create(tech_name="Test Tech A", used_at=resume_object)

    def test_tech_used_list_get(self) -> None:
        pass

    def test_tech_used_detail_get(self) -> None:
        pass

    def test_tech_used_post(self) -> None:
        pass

    def test_tech_used_poor_format_post(self) -> None:
        pass
