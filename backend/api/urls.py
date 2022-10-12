from django.urls import path
from api import views

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:query>/', views.staff_detail),
    path('skill/', views.skill_list),
    path('course/',views.course_list),
    path('job_role/', views.role_list)
]