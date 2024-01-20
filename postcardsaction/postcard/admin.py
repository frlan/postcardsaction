from django.contrib import admin

# from django_markdown.admin import MarkdownModelAdmin
from .models import Country
from .models import Postcard
from .models import PostcardItem
from .models import Series
from .models import Tag
from .models import URL

admin.site.register(Country)
admin.site.register(PostcardItem)
admin.site.register(Series)
admin.site.register(URL)


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    list_display = ["title", "id", "published", "publishing_date"]
    search_fields = ("title",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
