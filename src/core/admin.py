from django.contrib import admin
from .models import University, Course, Student 

# Register your models here.
admin.site.register(University) 
admin.site.register(Course) 
admin.site.register(Student)