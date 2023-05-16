from django.db import models


class Instructor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    profile_picture = models.FileField()

class Category(models.Model):
    name = models.CharField(max_length=20)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cover_photo = models.FileField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    episode = models.IntegerField()
    thumbnail = models.FileField()

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    profile_picture = models.FileField()
    education = models.CharField(max_length=200)

class Enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)