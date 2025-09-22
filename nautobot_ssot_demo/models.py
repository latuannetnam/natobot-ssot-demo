"""Models for Nautobot Ssot Demo."""

# Django imports
from django.db import models

# Nautobot imports
from nautobot.apps.models import PrimaryModel, extras_features
from nautobot.dcim.models import BaseInterface, Interface
from nautobot.ipam.models import IPAddress, VLAN

# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://docs.nautobot.com/projects/core/en/stable/plugins/development/#database-models
# If you want to use the extras_features decorator please reference the following documentation
# https://docs.nautobot.com/projects/core/en/stable/development/core/model-checklist/#extras-features
@extras_features("custom_links", "custom_validators", "export_templates", "graphql", "webhooks")
class DemoSSoT(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Base model for Nautobot Ssot Demo app."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # additional model fields

    class Meta:
        """Meta class."""

        ordering = ["name"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Nautobot Ssot Demo"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Nautobot Ssot Demos"

    def __str__(self):
        """Stringify instance."""
        return self.name


@extras_features("custom_links", "custom_validators", "export_templates", "graphql", "webhooks")
class JuniperInterface(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Model for Juniper Interface."""
    interface = models.OneToOneField(
        to=Interface,
        on_delete=models.CASCADE,
        null=True,
        blank=True,        
        # primary_key=True,
    )
    # additional model fields
    vlan_tagging = models.BooleanField(default=False)
    flexible_vlan_tagging = models.BooleanField(default=False)
    router_vlan = models.ForeignKey(
        null=True,
        blank=True,
        to=VLAN,
        on_delete=models.SET_NULL,)

    class Meta:
        """Meta class."""

        ordering = ["interface", "vlan_tagging", "flexible_vlan_tagging", "router_vlan"]
        # ordering = ["vlan_tagging", "flexible_vlan_tagging", "router_vlan"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Juniper Interface"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Juniper Interfaces"

    def __str__(self):
        """Stringify instance."""
        return self.interface.name

