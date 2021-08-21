from django.db import models


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


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    linked_in_link = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'

    def __str__(self):
        return self.first_name


class TechnologyUsed(models.Model):
    tech_name = models.CharField(max_length=50)
    used_at = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="Resume")

    class Meta:
        verbose_name = 'Technology Used'
        verbose_name_plural = 'Technologies Used'

    def __str__(self):
        return self.tech_name
