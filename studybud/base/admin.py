from django.contrib import admin

# Register your models here.
from .models import Course, Outline, Results

admin.site.register(Course)
admin.site.register(Outline) 
admin.site.register(Results)