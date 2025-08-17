"""Forms for nautobot_ssot_demo."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_ssot_demo import models


class DemoSSoTForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """DemoSSoT creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.DemoSSoT
        fields = "__all__"


class DemoSSoTBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """DemoSSoT bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.DemoSSoT.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class DemoSSoTFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.DemoSSoT
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
