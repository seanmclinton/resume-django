from django.urls import path
from resume import views

urlpatterns = [
    path('resume/', views.resume_list),
    path('resume/<int:pk>/', views.resume_detail),
    path('contact_info/', views.contact_list),
]