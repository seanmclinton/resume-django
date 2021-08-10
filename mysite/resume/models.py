from django.db import models

# Create your models here.


class Resume(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    linked_in_link = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)

    class Meta:
        verbose_name = 'Personal Information'
        verbose_name_plural = 'Personal Information'

    def __str__(self):
        return self.first_name
