from django.contrib import admin
from enrollstudent.models import StudentModel
# Register your models here.
admin.site.register(StudentModel)
# @admin.register(User)
# class ShowDataAdmin(admin.ModelAdmin):
#     list_display = ('id','name','email','password')    