from rest_framework import serializers

from dashboard_core.models import Settings

class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Settings
        fields = ('preferred_color' , )