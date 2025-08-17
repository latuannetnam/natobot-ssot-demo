"""Filtering for nautobot_ssot_demo."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_ssot_demo import models


class DemoSSoTFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for DemoSSoT."""

    class Meta:
        """Meta attributes for filter."""

        model = models.DemoSSoT

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
