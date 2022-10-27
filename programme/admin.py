from django.contrib import admin

from .models import Programme


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = [
        'date',
    ]


admin.site.register(Programme, ProgrammeAdmin)
