from django.contrib import admin
from .models import company, employee, department, division, position

# Register your models here.

@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'department', 'position', 'is_active')
    search_fields = ('name', 'email')
    list_filter = ('company', 'department', 'position')

admin.site.register(company)
admin.site.register(department)
admin.site.register(division)
admin.site.register(position)
