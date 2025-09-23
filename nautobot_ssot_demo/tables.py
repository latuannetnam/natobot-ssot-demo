"""Tables for nautobot_ssot_demo."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn
from .template_code import INTERFACE_IPADDRESSES

from nautobot_ssot_demo import models


class DemoSSoTTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(
        models.DemoSSoT,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
    )

    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.DemoSSoT
        fields = (
            "pk",
            "name",
            "description",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "name",
        #     "description",
        # )


class JuniperInterfaceTable(BaseTable):
    # pylint: disable=R0903
    """Table for list view."""

    pk = ToggleColumn()
    interface = tables.Column(linkify=True)
    device = tables.Column(accessor="interface__device", verbose_name="Device", linkify=True)
    ip_addresses = tables.TemplateColumn(
        accessor="interface__ip_addresses",
        template_code=INTERFACE_IPADDRESSES,
        orderable=False,
        verbose_name="IP Addresses",
    )    
    class Meta(BaseTable.Meta):
        """Meta attributes."""

        model = models.JuniperInterface
        fields = (
            "pk",
            "interface",
            "device",
            "ip_addresses",
            "vlan_tagging",
            "flexible_vlan_tagging",
            "router_vlan",
        )

        # Option for modifying the columns that show up in the list view by default:
        # default_columns = (
        #     "pk",
        #     "interface",
        #     "vlan_tagging",
        #     "flexible_vlan_tagging",
        #     "router_vlan",
        # )
