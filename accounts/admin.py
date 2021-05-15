from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('name', 'surname','phone_number', 'email', 'date_joined', 'last_login')
    list_display_links = ('phone_number', 'email', 'name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
