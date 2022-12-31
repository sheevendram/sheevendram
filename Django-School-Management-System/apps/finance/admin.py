from django.contrib import admin
from apps.finance.models import Invoice,InvoiceItem,Receipt

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['invoice']}),
        ('Receipt information', {'fields': ['amount_paid','date_paid','comment'], 'classes': ['collapse']}),
    ]


    list_display = ('invoice', 'amount_paid','date_paid','comment',)
    search_fields = ['invoice']

    list_filter = ['invoice','date_paid']
admin.site.register(Receipt,QuestionAdmin)