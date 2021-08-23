from django.urls import path
from resume import views

urlpatterns = [
    path('job/', views.JobList.as_view(), name="job_list"),
    path('job/<int:pk>/', views.JobList.as_view(), name="job_detail"),
    path('contact_info/', views.ContactInfoList.as_view(), name="contact_list"),
    path('contact_info/<int:pk>/', views.ContactInfoDetail.as_view(), name="contact_detail"),
    path('tech_used/', views.TechnologyUsedList.as_view(), name="tech_used_list"),
    path('tech_used/<int:pk>/', views.TechnologyUsedDetail.as_view(), name="tech_used_detail"),
    path('teapot/', views.im_a_little_teapot, name="teapot")

]