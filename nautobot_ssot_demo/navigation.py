"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
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

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Nautobot Ssot Demo", items=tuple(items)),),
    ),
)
