from django.test import TestCase
from resume.models import *
import datetime
# Create your tests here.


class JobTestCases(TestCase):
    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Job.objects.create(job_title="Test Job A", company="Test Company A", description="Test Description A",
                              start_date=job_a_start_date, end_date=job_a_end_date)

    def test_job_created(self) -> None:
        test_object = Job.objects.get(job_title="Test Job A")
        self.assertEqual(test_object.description, "Test Description A")
        self.assertEqual(test_object.company, "Test Company A")

    def test_str_function(self) -> None:
        test_object = Job.objects.get(job_title="Test Job A")
        self.assertEqual(str(test_object), "Test Company A")


class ContactInfoTestCases(TestCase):
    def setUp(self) -> None:
        ContactInfo.objects.create(first_name="TestFirstName",
                                   last_name="TestLastName",
                                   city="TestCity",
                                   email="test@test.com",
                                   linked_in_link="testlink.com",
                                   bio="test_bio")

    def test_contact_created(self) -> None:
        test_object = ContactInfo.objects.get(first_name="TestFirstName")
        self.assertEqual(test_object.last_name, "TestLastName")
        self.assertEqual(test_object.city, "TestCity")
        self.assertEqual(test_object.email, "test@test.com")
        self.assertEqual(test_object.linked_in_link, "testlink.com")
        self.assertEqual(test_object.bio, "test_bio")

    def test_str_function(self) -> None:
        test_object = ContactInfo.objects.get(first_name="TestFirstName")
        self.assertEqual(str(test_object), "TestFirstName")


class TechnologyUsedTestCases(TestCase):
    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Job.objects.create(job_title="Test Job A",
                              company="Test Company A",
                              description="Test Description A",
                              start_date=job_a_start_date,
                              end_date=job_a_end_date)

        job_object = Job.objects.get(job_title="Test Job A")
        TechnologyUsed.objects.create(tech_name="Test Tech A", used_at=job_object)

    def test_tech_used_created(self) -> None:
        test_object = TechnologyUsed.objects.get(tech_name="Test Tech A")
        self.assertEqual(test_object.tech_name, "Test Tech A")
        self.assertEqual(test_object.used_at.job_title, "Test Job A")

    def test_str_function(self) -> None:
        test_object = TechnologyUsed.objects.get(tech_name="Test Tech A")
        self.assertEqual(str(test_object), "Test Tech A")