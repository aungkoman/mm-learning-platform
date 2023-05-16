from django.contrib import admin

from .models import Instructor, Category, Course, Lesson , Student, Enroll

admin.site.site_header = "MM Learning Platfrom"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "MM Learning Platfrom"


class InstructorAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'dob')

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('id','name')

class CourseAdmin(admin.ModelAdmin): 
    list_display = ('id','name')

class LessonAdmin(admin.ModelAdmin): 
    list_display = ('id','name', 'course_name')

    def course_name(self, obj):
        # Logic to generate the value for the custom column
        return obj.course.name

class StudentAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'dob')

class EnrollAdmin(admin.ModelAdmin): 
    list_display = ('id','student_name', 'course_name')

    def course_name(self, obj):
        return obj.course.name
    
    def student_name(self, obj):
        return obj.student.first_name + " " + obj.student.last_name

admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Enroll,EnrollAdmin)