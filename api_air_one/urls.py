# from django.urls import path

from . import views

# urlpatterns = [
#     path("city/", views.CityListCreateView.as_view()),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cities", views.CityViewSet)
router.register(r"planes", views.PlaneViewSet)
router.register(r"routes", views.RouteViewSet)
urlpatterns = router.urls
