from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    subtitle = models.CharField(max_length=150)
    author = models.CharField(max_length=100, blank=False, null=False)
    isbn = models.CharField(max_length=20, blank=False, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)

    def __str__(self) -> str:
        return self.title
