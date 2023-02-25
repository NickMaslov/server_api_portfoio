from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"places", views.PlaceViewSet)
router.register(r"categories", views.CategoryViewSet)
router.register(r"menu_items", views.MenuItemViewSet)
router.register(r"orders", views.OrderViewSet)

urlpatterns = router.urls
