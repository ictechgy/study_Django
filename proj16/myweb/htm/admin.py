from django.contrib import admin
from htm.models import htmTagTable

# Register your models here.
class htmTagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tag_name',
    )

admin.site.register(htmTagTable, htmTagAdmin)