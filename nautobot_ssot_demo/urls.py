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
    path("devices/<uuid:pk>/device_detail_tab_1/", views.DeviceDetailAppTabOne.as_view(), name="device_detail_tab_1"),
    path("devices/<uuid:pk>/juniperinterface_list/", views.JuniperInterfaceUIViewSet.as_view({'get': 'list'}), name="juniperinterface_list"),
]

urlpatterns += router.urls
