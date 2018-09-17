from django.contrib import admin

from .models import Company
from .forms import CompanyCreationForm


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyCreationForm

    list_display = ('name', 'email', 'phone', 'website', 'location')
    list_filter = ()
    fieldsets = ((None, {
        'fields': ('name', 'email', 'phone', 'website', 'location')
    }), )

    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('name', 'email', 'phone', 'website', 'location')
    }), )
    search_fields = ('name', 'email', 'phone', 'website', 'location')
    ordering = ()
    filter_horizontal = ()


admin.site.register(Company, CompanyAdmin)
