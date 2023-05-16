from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse

from .models import Course
# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return HttpResponse("Hello World")

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = course.lesson_set.all()
    context = {"course": course, "lessons" : lessons}
    return render(request, "courses/detail.html", context)
    # return HttpResponse("You're looking at course %s." % course_id)