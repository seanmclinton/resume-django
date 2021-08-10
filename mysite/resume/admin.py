from django.contrib import admin
from .models import Resume, PersonalInfo
# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list = ('job_title', 'company', 'description')


class PersonalInfoAdmin(admin.ModelAdmin):
    list = ('first_name', 'last_name', 'city')


admin.site.register(Resume, ResumeAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)