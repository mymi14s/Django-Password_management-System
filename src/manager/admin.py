from django.contrib import admin
from manager.models import Manager
# Register your models here.

class AdminManager(admin.ModelAdmin):
    list_display = ['id', 'user', 'website_name']
    list_filter = ['id', 'user', 'website_name']
    search_fields = ['id', 'user', 'website_name']

admin.site.register(Manager, AdminManager)
