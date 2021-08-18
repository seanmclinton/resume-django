from django.test import TestCase
from resume.models import Resume, ContactInfo
import datetime
# Create your tests here.


class ResumeTestCase(TestCase):
    def setUp(self) -> None:
        job_a_start_date = datetime.datetime(2020, 2, 4, 0, 0)
        job_a_end_date = datetime.datetime(2021, 1, 5, 0, 0)
        Resume.objects.create(job_title="Test Job A", company="Test Company A", description="Test Description A",
                              start_date=job_a_start_date, end_date=job_a_end_date)

    def test_resume_created(self) -> None:
        test_object = Resume.objects.get(job_title="Test Job A")
        self.assertEqual(test_object.description, "Test Description A")
        self.assertEqual(test_object.company, "Test Company A")

    def test_str_function(self) -> None:
        test_object = Resume.objects.get(company="Test Company A")
        self.assertEqual(str(test_object), "Test Job A")


class ContactInfoTestCase(TestCase):
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
