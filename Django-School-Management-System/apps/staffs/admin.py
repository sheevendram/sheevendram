from django.contrib import admin
from apps.staffs.models import Staff
from django.contrib.admin import AdminSite

# Register your models here.

admin.site.site_header = 'K.J.V.S School Administration'


admin.site.register(Staff)