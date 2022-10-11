from django.urls import path
from api import views

urlpatterns = [
    path('staff/', views.staff_list),
    path('staff/<int:query>/', views.staff_detail),
]