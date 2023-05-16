from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]