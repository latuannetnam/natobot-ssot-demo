"""Template extensions for nautobot_ssot_demo."""

from nautobot.apps.ui import TemplateExtension, Tab, DistinctViewTab, ObjectFieldsPanel, ObjectsTablePanel


from .tables import JuniperInterfaceTable


class DeviceExtraTabs(TemplateExtension):
    model = "dcim.device"

    object_detail_tabs = (
        Tab(
            weight=100,
            tab_id="example_app_inline_tab",
            label="Inline Tab",
            panels=[
                ObjectFieldsPanel(weight=100, fields="__all__"),
            ],
        ),
        DistinctViewTab(
            weight=200,
            tab_id="example_app_view_tab",
            label="View Tab",
            url_name="plugins:nautobot_ssot_demo:device_detail_tab_1",
            
        ),
        DistinctViewTab(
            weight=300,
            tab_id="juniper_interface_view_tab",
            label="Juniper Interfaces",
            url_name="plugins:nautobot_ssot_demo:juniperinterface_list",
            
        ),
    )


template_extensions = [DeviceExtraTabs]