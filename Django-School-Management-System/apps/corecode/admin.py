from django.contrib import admin
from apps.corecode.models import AcademicSession,AcademicTerm,SiteConfig,StudentClass,Subject
from apps.result.models import Result
admin.site.register(AcademicSession)
admin.site.register(AcademicTerm)
admin.site.register(SiteConfig)
admin.site.register(StudentClass)
admin.site.register(Subject)
admin.site.register(Result)