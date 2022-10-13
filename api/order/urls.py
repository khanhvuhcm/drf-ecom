from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path("", views.OrderView.as_view()),
    path('', include(router.urls)),
]