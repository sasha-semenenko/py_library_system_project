from django.urls import path
from borrowings.views import BorrowCreateView, BorrowDetailView, BorrowListView

app_name = "borrowings"

urlpatterns = [
    path("borrow-create/", BorrowCreateView.as_view(), name="borrow-create"),
    path("borrowings/", BorrowListView.as_view(), name="borrow-list"),
    path("borrowings/<int:pk>/", BorrowDetailView.as_view(), name="borrow-detail")
]
