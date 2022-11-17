from django.contrib import admin

from .models import Programme


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'nb_views',
    ]


admin.site.register(Programme, ProgrammeAdmin)
