from django.contrib import admin
from .models import Copyright
from .models import Holder
from .models import Licence


class HolderAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = [
        "name",
    ]


class LicenceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    list_filter = ("name", "slug")
    search_fields = ["name", "fields"]


admin.site.register(Copyright)
admin.site.register(Holder, HolderAdmin)
admin.site.register(Licence, LicenceAdmin)
