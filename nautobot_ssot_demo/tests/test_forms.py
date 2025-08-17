"""Test demossot forms."""

from django.test import TestCase

from nautobot_ssot_demo import forms


class DemoSSoTTest(TestCase):
    """Test DemoSSoT forms."""

    def test_specifying_all_fields_success(self):
        form = forms.DemoSSoTForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.DemoSSoTForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_demossot_is_required(self):
        form = forms.DemoSSoTForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
