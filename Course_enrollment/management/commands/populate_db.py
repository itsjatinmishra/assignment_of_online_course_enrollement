from django.core.management.base import BaseCommand
from Course_enrollment.models import User, Course, Module, Enrollment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Enrollment.objects.all().delete()
        Module.objects.all().delete()
        Course.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        instructors_data = [
            {'name': 'Nazz', 'email': 'nazz@example.com'},
            {'name': 'Nikhil', 'email': 'nikhil@example.com'},
        ]

        students_data = [
            {'name': 'Gunn', 'email': 'gunn@example.com'},
            {'name': 'Jatin', 'email': 'jatin@example.com'},
            {'name': 'Lakhvinder', 'email': 'lakhvinder@example.com'},
            {'name': 'Maharshi', 'email': 'maharshi@example.com'},
        ]

        self.stdout.write('Creating instructors...')
        instructors = []
        for data in instructors_data:
            user = User.objects.create_user(
                username=data['email'].split('@')[0],
                email=data['email'],
                full_name=data['name'],
                password='password123',
                role=User.StatusChoice.INSTRUCTOR,
                is_staff=True
            )
            instructors.append(user)
            self.stdout.write(f'Created instructor: {user.full_name}')

        self.stdout.write('Creating students...')
        students = []
        for data in students_data:
            user = User.objects.create_user(
                username=data['email'].split('@')[0],
                email=data['email'],
                full_name=data['name'],
                password='password123',
                role=User.StatusChoice.STUDENT
            )
            students.append(user)
            self.stdout.write(f'Created student: {user.full_name}')

        self.stdout.write('Creating courses...')
        courses = []
        course_titles = ['Django for Beginners', 'Advanced REST Framework', 'System Design 101']
        
        for i, title in enumerate(course_titles):
            course = Course.objects.create(
                title=title,
                description=f'Learn everything about {title}',
                created_by=random.choice(instructors)
            )
            courses.append(course)
            self.stdout.write(f'Created course: {course.title}')

            for j in range(3):
                Module.objects.create(
                    course=course,
                    title=f'Module {j+1} for {title}',
                    duration_minutes=random.randint(30, 120)
                )

        self.stdout.write('Enrolling students...')
        for student in students:
        
            enrolled_courses = random.sample(courses, k=random.randint(1, 2))
            for course in enrolled_courses:
                Enrollment.objects.create(
                    student=student,
                    course=course,
                    status=random.choice([Enrollment.StatusChoice.ACTIVE, Enrollment.StatusChoice.COMPLETED])
                )
                self.stdout.write(f'Enrolled {student.full_name} in {course.title}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
