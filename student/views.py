from os import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Program, Student, CohortGroup, Student_Profile



# Create your views here.

def home_page(request):
    return render(request, 'indexmain.html')

def about_us(request):
    return render(request, 'about.html')


def all_students(request):
    students = Student.objects.all()
    return render(request, 'indexmain.html', {'students': students})

# Filter students by cohort
# def students_by_cohort(request, cohort_name):
#     students = Student.objects.filter(cohort_name=cohort_name)
#     return render(request, 'indexmain.html', {'students': students})

def students_by_cohort(request, cohort_name):
    # Get all cohorts that match the cohort_name
    cohorts = CohortGroup.objects.filter(name=cohort_name)
    
    #if cohorts.exists():
        # Collect all students in these cohorts
    students = Student.objects.filter(cohortgroup__in=cohorts)
    #else:
        #students = None  # or handle the case where no cohort matches
    
    return render(request, 'indexmain.html', {'students': students})

# Query students based on the program courses
def students_by_course(request, course_name):
    # Filter students by the course they are enrolled in
    students = Student.objects.filter(program__courses__icontains=course_name).distinct()
    
    return render(request, 'indexmain.html', {'students': students, 'course': course_name})

def students_by_type(request, type_name):
    students = Student.objects.filter(student_profile__student_types=type_name)
    return render(request, 'indexmain.html', {'students': students})

