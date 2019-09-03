from django.contrib import admin

from control.users.models import BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "address",
        "email",
        "phone_number",
    ]
