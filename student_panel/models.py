from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.roll_number}"

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration_weeks = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments_course')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress_percentage = models.FloatField(default=0)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.user.email} - {self.course.title}"


# Assignment Model
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.course.title})"


# Submission Model
class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions_assignment')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions_student')
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    graded = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.email} - {self.assignment.title}"
