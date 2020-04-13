from django.contrib import admin
from .models import PCPostCard
from .models import PCUser


@admin.register(PCPostCard)
class PCPostCardAdmin(admin.ModelAdmin):
    list_display = ["pc_id", "id", "from_user"]


@admin.register(PCUser)
class PCUserAdmin(admin.ModelAdmin):
    list_display = ["username"]
