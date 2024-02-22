from django.contrib.auth import get_user_model
from rest_framework import generics

from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserManageView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
