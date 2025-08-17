"""API serializers for nautobot_ssot_demo."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_ssot_demo import models


class DemoSSoTSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """DemoSSoT Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.DemoSSoT
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
