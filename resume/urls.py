from django.urls import path
from resume import views

urlpatterns = [
    path('resume/', views.resume_list, name="resume_list"),
    path('resume/<int:pk>/', views.resume_detail, name="resume_detail"),
    path('contact_info/', views.contact_list, name="contact_list"),
    path('contact_info/<int:pk>/', views.contact_detail, name="contact_detail"),
    path('tech_used/', views.techology_used_list, name="tech_used_list"),
    path('tech_used/<int:pk>/', views.technology_used_detail, name="tech_used_detail"),

]