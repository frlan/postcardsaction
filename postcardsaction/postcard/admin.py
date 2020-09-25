from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from .models import Postcard
from .models import PostcardItem
from .models import Tag
from .models import URL
from .models import Series

admin.site.register(URL)
admin.site.register(PostcardItem)
admin.site.register(Series)


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    list_display = ["description_short", "id", "published"]
    search_fields = ("description_short", )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
