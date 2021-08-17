from django.contrib import admin
from .models import Resume, ContactInfo
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list = ('job_title', 'company', 'description')


class ContactInfoAdmin(admin.ModelAdmin):
    list = ('first_name', 'last_name', 'city')


admin.site.register(Resume, ResumeAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)