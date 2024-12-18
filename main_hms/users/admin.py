from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "slug", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ["username", "email"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("username",)}
