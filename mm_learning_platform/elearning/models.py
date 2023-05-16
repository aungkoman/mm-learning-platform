from django.db import models


class Instructor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    profile_picture = models.FileField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    cover_photo = models.FileField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()
    episode = models.IntegerField()
    thumbnail = models.FileField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    profile_picture = models.FileField()
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.first_name + " -> " + self.course.name