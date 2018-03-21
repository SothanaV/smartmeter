from django.contrib import admin
from .models import Pressure,Document
# Register your models here.
class PressureAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Pressure._meta.fields]
admin.site.register(Pressure,PressureAdmin)

class DocumentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Document._meta.fields]
admin.site.register(Document,DocumentAdmin)