from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Postcard
from .models import Tag
from .models import URL

admin.site.register(URL)

@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    list_display = ["id", "description_short"]
    search_fields = ("description_short",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
