from django.contrib import admin
from nautobot.apps.admin import NautobotModelAdmin

from .models import JuniperInterface
@admin.register(JuniperInterface)
class JuniperInterfaceAdmin(NautobotModelAdmin):
    list_display = ("get_interface_name", "vlan_tagging", "flexible_vlan_tagging", "router_vlan")
    list_filter = ("interface__name",)
    
    def get_interface_name(self, obj):
        """Return the name of the associated interface."""
        return obj.interface.name if obj.interface else "No Interface"
    
    get_interface_name.short_description = "Interface Name"
    get_interface_name.admin_order_field = "interface__name"
