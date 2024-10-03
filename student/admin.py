from django.contrib import admin

# Studen/admin.py

from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('first_name', 'last_name', 'enrollment_date')


admin.site.register(Student, StudentAdmin)