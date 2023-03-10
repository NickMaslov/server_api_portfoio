from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"products", views.ProductViewSet)

urlpatterns = router.urls
