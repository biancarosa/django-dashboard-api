from django.contrib.auth.models import User
from rest_framework import routers, viewsets

from dashboard_api.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer