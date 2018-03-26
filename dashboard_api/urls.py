"""dashboard_api URL Configuration"""
from django.conf.urls import url, include

from rest_framework import routers, viewsets

from dashboard_core.views.user import UserViewSet
from dashboard_core.views.settings import SettingsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'settings', SettingsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]