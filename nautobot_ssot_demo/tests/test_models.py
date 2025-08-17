"""Test DemoSSoT."""

from nautobot.apps.testing import ModelTestCases

from nautobot_ssot_demo import models
from nautobot_ssot_demo.tests import fixtures


class TestDemoSSoT(ModelTestCases.BaseModelTestCase):
    """Test DemoSSoT."""

    model = models.DemoSSoT

    @classmethod
    def setUpTestData(cls):
        """Create test data for DemoSSoT Model."""
        super().setUpTestData()
        # Create 3 objects for the model test cases.
        fixtures.create_demossot()

    def test_create_demossot_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        demossot = models.DemoSSoT.objects.create(name="Development")
        self.assertEqual(demossot.name, "Development")
        self.assertEqual(demossot.description, "")
        self.assertEqual(str(demossot), "Development")

    def test_create_demossot_all_fields_success(self):
        """Create DemoSSoT with all fields."""
        demossot = models.DemoSSoT.objects.create(name="Development", description="Development Test")
        self.assertEqual(demossot.name, "Development")
        self.assertEqual(demossot.description, "Development Test")
