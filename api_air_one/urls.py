from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"cities", views.CityViewSet)
router.register(r"planes", views.PlaneViewSet)
router.register(r"routes", views.RouteViewSet)
urlpatterns = router.urls
