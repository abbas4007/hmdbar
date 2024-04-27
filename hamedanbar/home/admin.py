from django.contrib import admin
from .models import Category,Video,Course
# Register your models here.
admin.site.register(Video)
admin.site.register(Course)