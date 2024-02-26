from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView
)

from users.views import CreateUserView, UserManageView, UserListView

urlpatterns = [
    path("users/", CreateUserView.as_view(), name="register"),
    path("users/me/", UserManageView.as_view(), name="manage"),
    path("users-list/", UserListView.as_view(), name="user-list"),

    # Token authentication

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify")
]

app_name = "users"
