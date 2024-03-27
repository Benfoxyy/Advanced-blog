from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('email','is_superuser','is_active',)
    list_filter = ("email", "is_staff", "is_active",)
    ordering = ('email',)
    search_fields = ('email',)

    fieldsets = (
        ("Authentication", {
            "fields": (
                'email','password'
            ),
        }),
        ("Permission", {
            "fields":(
                "is_superuser", "is_staff", "is_active",
            ),
        }),
        ("Group Permission", {
            "fields":(
                "groups", "user_permissions",
            ),
        }),
        ("Important_date", {
            "fields":(
                "last_login",
            ),
        }),
    )
    
    add_fieldsets = (
        ("Form", {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active","is_superuser",
            )}
        ),
    )

admin.site.register(User,CustomUserAdmin)