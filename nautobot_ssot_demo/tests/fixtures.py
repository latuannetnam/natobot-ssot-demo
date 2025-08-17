"""Create fixtures for tests."""

from nautobot_ssot_demo.models import DemoSSoT


def create_demossot():
    """Fixture to create necessary number of DemoSSoT for tests."""
    DemoSSoT.objects.create(name="Test One")
    DemoSSoT.objects.create(name="Test Two")
    DemoSSoT.objects.create(name="Test Three")
