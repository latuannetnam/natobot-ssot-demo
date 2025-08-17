"""API views for nautobot_ssot_demo."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_ssot_demo import filters, models
from nautobot_ssot_demo.api import serializers


class DemoSSoTViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """DemoSSoT viewset."""

    queryset = models.DemoSSoT.objects.all()
    serializer_class = serializers.DemoSSoTSerializer
    filterset_class = filters.DemoSSoTFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
