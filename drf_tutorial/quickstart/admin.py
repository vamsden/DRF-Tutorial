from django.contrib import admin
from .models import User, Group

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['url', 'username', 'email', 'groups']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['url', 'name']

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
