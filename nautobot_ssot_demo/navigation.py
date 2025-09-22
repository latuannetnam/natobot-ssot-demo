"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

# Items for the Apps tab
app_items = (
    NavMenuItem(
        link="plugins:nautobot_ssot_demo:demossot_list",
        name="Nautobot Ssot Demo",
        permissions=["nautobot_ssot_demo.view_demossot"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_ssot_demo:demossot_add",
                permissions=["nautobot_ssot_demo.add_demossot"],
            ),
        ),
    ),
)

# Juniper Interfaces menu item for the Devices tab
juniper_interfaces_item = NavMenuItem(
    link="plugins:nautobot_ssot_demo:juniperinterface_list",
    name="Juniper Interfaces",
    weight=150,
    permissions=["nautobot_ssot_demo.view_juniperinterface"],
    buttons=(
        NavMenuAddButton(
            link="plugins:nautobot_ssot_demo:juniperinterface_add",
            permissions=["nautobot_ssot_demo.add_juniperinterface"],
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Nautobot Ssot Demo", items=tuple(app_items)),),
    ),
    NavMenuTab(
        name="Devices",
        weight=200,
        groups=(
            NavMenuGroup(
                name="Device Components",
                weight=600,
                items=(juniper_interfaces_item,),
            ),
        ),
    ),
)
