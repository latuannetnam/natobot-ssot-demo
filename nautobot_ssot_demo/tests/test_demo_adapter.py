"""Test Demo adapter."""

import json
import uuid
from unittest.mock import MagicMock

from django.contrib.contenttypes.models import ContentType
from nautobot.extras.models import Job, JobResult
from nautobot.core.testing import TransactionTestCase
from nautobot_ssot_demo.diffsync.adapters import DemoRemoteAdapter
from nautobot_ssot_demo.jobs import DemoDataSource


def load_json(path):
    """Load a json file."""
    with open(path, encoding="utf-8") as file:
        return json.loads(file.read())


DEVICE_FIXTURE = load_json("./nautobot_ssot_demo/tests/fixtures/get_devices.json")


class TestDemoAdapterTestCase(TransactionTestCase):
    """Test NautobotSsotDemoAdapter class."""

    databases = ("default", "job_logs")

    def setUp(self):  # pylint: disable=invalid-name
        """Initialize test case."""
        self.demo_client = MagicMock()
        self.demo_client.get_devices.return_value = DEVICE_FIXTURE

        self.job = DemoDataSource()
        self.job.job_result = JobResult.objects.create(name=self.job.class_path)
        self.demo = DemoRemoteAdapter(job=self.job, sync=None, client=self.demo_client)

    def test_data_loading(self):
        """Test Nautobot Ssot Demo load() function."""
        # self.demo.load()
        # self.assertEqual(
        #     {dev["name"] for dev in DEVICE_FIXTURE},
        #     {dev.get_unique_id() for dev in self.demo.get_all("device")},
        # )
