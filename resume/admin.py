from django.contrib import admin
from .models import *
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list = ('job_title', 'company', 'description')


class ContactInfoAdmin(admin.ModelAdmin):
    list = ('first_name', 'last_name', 'city')


class TechnologyUsedAdmin(admin.ModelAdmin):
    list = ('tech_name', 'used_at')


admin.site.register(Job, JobAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(TechnologyUsed, TechnologyUsedAdmin)