from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','department','student_id']

class MarksAdminn(admin.ModelAdmin):
    list_display = ['subject','marks','student']    


admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student,StudentAdmin)
admin.site.register(Subject)
admin.site.register(StudentMark,MarksAdminn)

