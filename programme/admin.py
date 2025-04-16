from django.contrib import admin
from django.utils.html import format_html

from .models import Programme


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'nb_views',
        'view_url',
    ]

    def view_url(self, obj):
        return format_html('<a href="{}" target="_blank">Voir</a>', obj.get_absolute_url())

    view_url.short_description = 'URL'


admin.site.register(Programme, ProgrammeAdmin)
