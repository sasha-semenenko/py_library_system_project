from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    class CoverBookChoices(models.TextChoices):
        HARD = "hard", _("HARD")
        SOFT = "soft", _("SOFT")

    title = models.CharField(max_length=65, unique=True)
    author = models.CharField(max_length=65, unique=True)
    cover = models.CharField(max_length=65, choices=CoverBookChoices.choices)
    inventory = models.IntegerField()
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
