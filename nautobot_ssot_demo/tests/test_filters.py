"""Test DemoSSoT Filter."""

from nautobot.apps.testing import FilterTestCases

from nautobot_ssot_demo import filters, models
from nautobot_ssot_demo.tests import fixtures


class DemoSSoTFilterTestCase(FilterTestCases.FilterTestCase):
    """DemoSSoT Filter Test Case."""

    queryset = models.DemoSSoT.objects.all()
    filterset = filters.DemoSSoTFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for DemoSSoT Model."""
        fixtures.create_demossot()

    def test_q_search_name(self):
        """Test using Q search with name of DemoSSoT."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for DemoSSoT."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
