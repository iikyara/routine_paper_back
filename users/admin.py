from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, FirebaseUser


admin.site.register(User, UserAdmin)


@admin.register(FirebaseUser)
class FirebaseUserAdmin(admin.ModelAdmin):
    pass
