from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('staff/', views.staff_list.as_view()),
    path('staff/<int:pk>/', views.staff_detail.as_view()),
#################################################################################################
    path('skill/', views.skill_list.as_view()),
    path('skill/<int:pk>/', views.skill_detail.as_view()),
################################################################################################
    path('course/',views.course_list.as_view()),
    path('course/<str:pk>/',views.course_detail.as_view()),
#################################################################################################
    path('skill_to_course/<int:pk>/',views.skill_assign_course_detail.as_view()),
    path('skill_to_course/<int:skill>/<str:course>/',views.skill_assign_course_detail.as_view()),
####################################################################################################
    path('user_role/',views.user_role_list.as_view()),
####################################################################################################
    path('registration/',views.registration_list.as_view()),
    path('registration/<int:pk>/',views.registration_detail.as_view()),
    path('registration/<str:pk>/',views.registration_detail.as_view()),
###################################################################################################
    path('job_role/',views.job_role_list.as_view()),
    path('job_role/<int:pk>/',views.job_role_detail.as_view()),
###################################################################################################
    path('skill_to_job_role/<int:skill>/<int:job_role>/',views.job_assign_skill_detail.as_view()),
#####################################################################################################
    path('req/<int:staff_id>/',views.requirements_list.as_view()),
    path('req/<int:staff_id>/<int:job_role_id>/',views.requirements_list.as_view()),
###################################################################################################
    path('skill_attained/<int:staff_id>/', views.Skill_Attained.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

