from .serializers import UserSerializer
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-id')

    def get_permissions(self):
        permission = AllowAny() if self.action in ('create',) else IsAdminUser()
        print(self.action)
        return [permission]
