from django.contrib.auth.models import User
from rest_framework import viewsets
from dashboard_core.serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer