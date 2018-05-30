from django.contrib import admin
from .models import Teacher, Standard, Timetable
# Register your models here.
admin.site.register(Standard)
admin.site.register(Teacher)
admin.site.register(Timetable)
