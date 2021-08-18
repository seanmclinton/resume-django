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

    def test_resume_created(self):
        test_object = Resume.objects.get(job_title="Test Job A")
        self.assertEqual(test_object.description, "Test Description A")
        self.assertEqual(test_object.company, "Test Company A")


class ContactInfoTestCase(TestCase):
    pass
