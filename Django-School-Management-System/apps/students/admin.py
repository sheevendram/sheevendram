from django.contrib import admin
from apps.students.models import Student
from django.contrib.admin import AdminSite

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = 'KJVS SCHOOL Administration'


admin.site.register(Student)

# Register your models here.
