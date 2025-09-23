"""Tables for nautobot_ssot_demo."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn

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
    ip_addresses = tables.Column(accessor="interface__ip_addresses", verbose_name="IP Address")
    
    def render_ip_addresses(self, record):
        """Render IP addresses as a comma-separated list."""
        ip_addresses = record.interface.ip_addresses.all()
        if not ip_addresses:
            return "—"
        
        # Format IP addresses as comma-separated list
        ip_strings = [str(ip) for ip in ip_addresses]
        return ", ".join(ip_strings)
    actions = ButtonsColumn(
        models.JuniperInterface,
        # Option for modifying the default action buttons on each row:
        # buttons=("changelog", "edit", "delete"),
        # Option for modifying the pk for the action buttons:
        pk_field="pk",
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
