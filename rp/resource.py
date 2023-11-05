from import_export import resources
from .models import Kategoriya


class KategoriyaResource(resources.ModelResource):
    class Meta:
        model = Kategoriya
