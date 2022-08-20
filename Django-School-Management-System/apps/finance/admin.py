from django.contrib import admin
from apps.finance.models import Invoice,InvoiceItem,Receipt

# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Receipt)