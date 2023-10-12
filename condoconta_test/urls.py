from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"accounts", views.AccountViewSet)
router.register(r"transactions", views.TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
