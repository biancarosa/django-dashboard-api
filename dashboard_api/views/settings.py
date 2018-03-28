from rest_framework import viewsets

from dashboard_api.models import Settings
from dashboard_api.serializers.settings import SettingsSerializer
        
class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer