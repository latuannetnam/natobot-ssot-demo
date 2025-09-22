"""Django urlpatterns declaration for nautobot_ssot_demo app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from nautobot_ssot_demo import views


app_name = "nautobot_ssot_demo"
router = NautobotUIViewSetRouter()

# The standard is for the route to be the hyphenated version of the model class name plural.
# for example, ExampleModel would be example-models.
router.register("demo-ss-o-ts", views.DemoSSoTUIViewSet)
router.register("juniper-interfaces", views.JuniperInterfaceUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("nautobot_ssot_demo/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
