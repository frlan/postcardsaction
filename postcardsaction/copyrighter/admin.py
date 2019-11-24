from django.contrib import admin
from .models import Copyright
from .models import Holder
from .models import Licence


admin.site.register(Copyright)
admin.site.register(Holder)
admin.site.register(Licence)
