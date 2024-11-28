from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class StudentProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response({'error': 'Student profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            student = Student.objects.get(user=request.user)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'error': 'Student profile not found'}, status=status.HTTP_404_NOT_FOUND)


class CourseListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class EnrollmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ensure the student is retrieved from the authenticated user
        student = request.user.student
        data = request.data.copy()
        data['student'] = student.id  # Associate the student with the enrollment
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Get all enrollments for the current student
        student = request.user.student
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)


class AssignmentSubmissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Ensure the student is retrieved from the authenticated user
        student = request.user.student
        data = request.data.copy()
        data['student'] = student.id  # Associate the student with the assignment submission
        serializer = AssignmentSubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Get all assignment submissions for the current student
        student = request.user.student
        submissions = AssignmentSubmission.objects.filter(student=student)
        serializer = AssignmentSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)
