"""Django API urlpatterns declaration for nautobot_ssot_demo app."""

from nautobot.apps.api import OrderedDefaultRouter

from nautobot_ssot_demo.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("demo-ss-o-ts", views.DemoSSoTViewSet)

app_name = "nautobot_ssot_demo-api"
urlpatterns = router.urls
