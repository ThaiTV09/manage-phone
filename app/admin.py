from django.contrib import admin
from .models import *


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['serial']
    search_fields = ['serial']
    list_filter = ['serial']
admin.site.register(Phone,PhoneAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['department']
    search_fields = ['department']
    list_filter = ['department']
admin.site.register(Department,CompanyAdmin)

class PhoneItemAdmin(admin.ModelAdmin):
    list_display = ['serial']
    search_fields = ['serial']
    list_filter = ['serial']
admin.site.register(PhoneItem,PhoneItemAdmin)