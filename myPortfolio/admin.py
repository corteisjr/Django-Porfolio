from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'gitHub_link', 'link', 'projectType' )
    data_hierarchy = 'created_at'

admin.site.register(Projectos, ProfileAdmin)
