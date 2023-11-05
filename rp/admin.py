from django.contrib import admin
from rp.models import Kategoriya
from import_export.admin import ImportExportModelAdmin
from .resource import KategoriyaResource


class KategoriyaAdmin(ImportExportModelAdmin):
    resource_class = KategoriyaResource


admin.site.register(Kategoriya, KategoriyaAdmin)
# Register your models here.
