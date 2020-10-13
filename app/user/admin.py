from django.contrib import admin
from app.user.models import User, Contact


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name',
                    'group', 'superuser', 'staff', 'active']

    search_fields = ['username', 'first_name', 'last_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'date_added']


admin.site.register(User, UserAdmin)
admin.site.register(Contact, ContactAdmin)
