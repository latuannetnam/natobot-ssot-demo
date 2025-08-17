"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot_ssot_demo import models
from nautobot_ssot_demo.tests import fixtures


class DemoSSoTViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the DemoSSoT views."""

    model = models.DemoSSoT
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_demossot()
