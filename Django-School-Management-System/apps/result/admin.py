from django.contrib import admin
from apps.result.models import Result
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['student','session','term','current_class']}),
        ('Result information', {'fields': ['subject','test_score','exam_score'], 'classes': ['collapse']}),
    ]


    list_display = ('student', 'current_class','subject','test_score','exam_score')
    search_fields = ['subject']

    list_filter = ['student','subject','current_class','term']
admin.site.register(Result,QuestionAdmin)