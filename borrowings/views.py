from rest_framework import generics

from borrowings.models import Borrowing
from borrowings.serializers import BorrowingSerializer, BorrowingDetailSerializer, BorrowingListSerializer


class BorrowCreateView(generics.CreateAPIView):
    queryset = Borrowing.objects.select_related("book_id", "user_id")
    serializer_class = BorrowingSerializer

    def perform_create(self, serializer):
        serializer.save(user_id = self.request.user)


class BorrowDetailView(generics.RetrieveDestroyAPIView):
    queryset = Borrowing.objects.select_related("book_id", "user_id")
    serializer_class = BorrowingDetailSerializer


class BorrowListView(generics.ListAPIView):
    queryset = Borrowing.objects.select_related("book_id", "user_id")
    serializer_class = BorrowingListSerializer
