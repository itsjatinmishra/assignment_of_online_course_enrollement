from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/modules/', views.ModuleListCreateView.as_view(), name='module-list'),
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/create/', views.EnrollmentCreateView.as_view(), name='enrollment-create'),
]
