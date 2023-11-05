from django.contrib import admin
from .models import Type_task, Otdels, Tasks
from import_export.admin import ImportExportModelAdmin
from .resource import Type_taskResource, OtdelsResource, TasksResource


@admin.register(Tasks)
class TasksAdmin(ImportExportModelAdmin):
    resource_class = TasksResource


@admin.register(Otdels)
class OtdelsAdmin(ImportExportModelAdmin):
    resource_class = OtdelsResource


@admin.register(Type_task)
class TaskAdmin(ImportExportModelAdmin):
    resource_class = Type_taskResource


# admin.site.register([Type_task, Otdels, Tasks],
#                     TaskAdmin)


# Register your models here.
