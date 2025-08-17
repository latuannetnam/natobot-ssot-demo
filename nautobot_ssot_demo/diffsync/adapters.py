"""Diffsync adapters for nautobot_ssot_demo."""

from diffsync import Adapter
from nautobot_ssot.contrib import NautobotAdapter

from nautobot_ssot_demo.diffsync.models import DeviceSSoTModel


class DemoRemoteAdapter(Adapter):
    """DiffSync adapter for Demo."""

    device = DeviceSSoTModel

    top_level = ["device"]

    def __init__(self, *args, job=None, sync=None, client=None, **kwargs):
        """Initialize Demo.

        Args:
            job (object, optional): Demo job. Defaults to None.
            sync (object, optional): Demo SSoT. Defaults to None.
            client (object): Demo API client connection object.
        """
        super().__init__(*args, **kwargs)
        self.job = job
        self.sync = sync
        self.conn = client

    def load(self):
        """Load data from Demo into SSoT models."""
        test_device = self.device(name="Test Device",
                                status__name="Active",
                                role__name="Router",                                      
                                device_type__model="Cisco Router",
                                location__name="Vietnam", 
                                example_custom_field="Test Field value")
        self.add(test_device)


class DemoNautobotAdapter(NautobotAdapter):
    """DiffSync adapter for Nautobot."""

    device = DeviceSSoTModel

    top_level = ["device"]

    
