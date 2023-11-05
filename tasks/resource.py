from import_export import resources
from .models import Type_task, Otdels, Tasks


class Type_taskResource(resources.ModelResource):
    class Meta:
        model = Type_task


class OtdelsResource(resources.ModelResource):
    class Meta:
        model = Otdels


class TasksResource(resources.ModelResource):
    class Meta:
        model = Tasks
