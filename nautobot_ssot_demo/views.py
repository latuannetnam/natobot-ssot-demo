"""Views for nautobot_ssot_demo."""

from nautobot.apps.views import NautobotUIViewSet

from nautobot_ssot_demo import filters, forms, models, tables
from nautobot_ssot_demo.api import serializers


class DemoSSoTUIViewSet(NautobotUIViewSet):
    """ViewSet for DemoSSoT views."""

    bulk_update_form_class = forms.DemoSSoTBulkEditForm
    filterset_class = filters.DemoSSoTFilterSet
    filterset_form_class = forms.DemoSSoTFilterForm
    form_class = forms.DemoSSoTForm
    lookup_field = "pk"
    queryset = models.DemoSSoT.objects.all()
    serializer_class = serializers.DemoSSoTSerializer
    table_class = tables.DemoSSoTTable


class JuniperInterfaceUIViewSet(NautobotUIViewSet):
    """ViewSet for JuniperInterface views."""

    bulk_update_form_class = forms.JuniperInterfaceBulkEditForm
    filterset_class = filters.JuniperInterfaceFilterSet
    filterset_form_class = forms.JuniperInterfaceFilterForm
    form_class = forms.JuniperInterfaceForm
    lookup_field = "pk"
    queryset = models.JuniperInterface.objects.all()
    serializer_class = serializers.JuniperInterfaceSerializer
    table_class = tables.JuniperInterfaceTable
