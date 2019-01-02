from django.contrib import admin
from django.contrib import auth
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email','date_joined']
    list_filter = ['username', 'first_name', 'last_name', 'email','date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email','date_joined']
    #list_editable = ['email']

register = admin.site.register #shorten the module name
#register(User, AdminUser)

# class AdminUser(admin.ModelAdmin):
#     list_display = ['username', 'first_name', 'last_name', 'email','date_joined']
#     list_filter = ['username', 'first_name', 'last_name', 'email','date_joined']
#     search_fields = ['username', 'first_name', 'last_name', 'email','date_joined']
#     #list_editable = ['email']

# register(Profile)
