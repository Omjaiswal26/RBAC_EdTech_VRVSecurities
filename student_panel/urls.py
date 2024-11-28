from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentProfileAPIView.as_view(), name="student-profile"),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('enrollments/', EnrollmentAPIView.as_view(), name='enrollment'),
    path('submissions/', AssignmentSubmissionAPIView.as_view(), name='assignment-submission'),
]
