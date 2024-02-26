from rest_framework import serializers

from books.serializers import BookSerializer
from borrowings.models import Borrowing
from users.serializers import UserSerializer

class BorrowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id"
        ]

    def validate(self, attrs):
        data = super(BorrowingSerializer, self).validate(attrs)

        Borrowing.validate_book_inventory(attrs["book_id"].inventory, serializers.ValidationError)

        return data


class BorrowingListSerializer(BorrowingSerializer):
    book_title = serializers.CharField(source="book_id.title", read_only=True)
    book_inventory = serializers.CharField(source="book_id.inventory", read_only=True)
    user_email= serializers.CharField(source="user_id.email", read_only=True)

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_title",
            "book_inventory",
            "user_email"
        ]


class BorrowingDetailSerializer(BorrowingSerializer):
    book_id = BookSerializer(many=False, read_only=True)
    user_id = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Borrowing
        fields = [
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book_id",
            "user_id"
        ]
