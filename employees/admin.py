from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('email', 'phone', 'company', 'user', 'github', 'linkedin')
    list_filter = ()
    fieldsets = ((None, {
        'fields': ('email', 'phone', 'company', 'user')
    }), )

    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('email', 'phone', 'company', 'user')
    }), )
    search_fields = ('email',)
    ordering = ()
    filter_horizontal = ()


admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Group)
