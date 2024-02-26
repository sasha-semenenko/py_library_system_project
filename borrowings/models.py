from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint

from books.models import Book


class Borrowing(models.Model):
    borrow_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-borrow_date"]
        verbose_name = "borrowing"
        verbose_name_plural = "borrowings"
        constraints = [
            UniqueConstraint(
                name="borrowing_constraints",
                fields=["borrow_date", "expected_return_date", "actual_return_date"]
            )
        ]
    def __str__(self) -> str:
        return f"Borrow {self.book_id.title} at {self.borrow_date} and should return at {self.expected_return_date}"

    @staticmethod
    def validate_book_inventory(inventory: int, error_to_raise):
        if inventory < 0:
            raise error_to_raise(f"Inventory book is {inventory} that is not equal or more 0")

    def clean(self):
        Borrowing.validate_book_inventory(self.book_id.inventory, ValidationError)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.book_id.inventory -= 1
        self.full_clean()
        self.book_id.save()
        return super(Borrowing, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)
