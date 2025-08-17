"""App declaration for nautobot_ssot_demo."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class NautobotSsotDemoConfig(NautobotAppConfig):
    """App configuration for the nautobot_ssot_demo app."""

    name = "nautobot_ssot_demo"
    verbose_name = "Nautobot Ssot Demo"
    version = __version__
    author = "Le Anh Tuan"
    description = "Nautobot Ssot Demo."
    base_url = "ssot-demo"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:nautobot_ssot_demo:docs"


config = NautobotSsotDemoConfig  # pylint:disable=invalid-name
