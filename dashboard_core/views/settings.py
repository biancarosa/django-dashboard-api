from rest_framework import viewsets

from dashboard_core.models import Settings
from dashboard_core.serializers.settings import SettingsSerializer
        
class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer