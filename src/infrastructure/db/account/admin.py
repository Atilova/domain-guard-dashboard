from django.contrib import admin

from .models import AppUser, RefreshToken

from infrastructure.adminsite.account import AppUserAdmin


admin.site.register(AppUser, AppUserAdmin)
admin.site.register(RefreshToken)