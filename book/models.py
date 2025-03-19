from author.models import Author
import re
from django.db import models
from django.core.exceptions import ValidationError
Q = models.Q


class BookManager(models.Manager):
    def filter_book(self, pk_author, status):
        books = self.all()
        available_authors = Author.objects.all()

        if status == 'available' or status == 'on_loan':
            books = books.filter(status=status)
            available_authors = Author.objects.filter(
                book_author__status=status).distinct()

        if pk_author and pk_author.isdigit():
            books = books.filter(author=pk_author)

        return books, available_authors

    def search_title_isbn(self, search):
        books = self.filter(
            Q(title__icontains=search) |
            Q(isbn__icontains=search)
        )
        return books


def validate_ibns(value):
    regex = r"^\d{9}[\dX]$|^\d{13}$"
    isbn = value.replace("-", "").replace(" ", "")

    if not re.fullmatch(regex, isbn):
        raise ValidationError("O ISBN deve ter 10 ou 13 dígitos.")

    if len(isbn) == 10:  # Validação ISBN-10
        total = sum((10 - i) * (10 if x == "X" else int(x))
                    for i, x in enumerate(isbn))
        if total % 11 != 0:
            raise ValidationError("O ISBN-10 informado não é válido.")

    elif len(isbn) == 13:  # Validação ISBN-13
        total = sum((1 if i % 2 == 0 else 3) * int(x)
                    for i, x in enumerate(isbn))
        if total % 10 != 0:
            raise ValidationError("O ISBN-13 informado não é válido.")


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'disponível'),
        ('on_loan', 'emprestado'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='book_author')
    isbn = models.CharField(max_length=16, unique=True,
                            validators=[validate_ibns])
    publication_date = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='available',)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BookManager()

    def __str__(self):
        return f"{self.title} ({self.isbn})"
