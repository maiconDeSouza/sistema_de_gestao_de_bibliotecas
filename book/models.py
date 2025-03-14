from django.db import models

from author.models import Author
# Create your models here.


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'disponível'),
        ('on_loan', 'emprestado'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='book_author')
    isbn = models.CharField(max_length=16, unique=True)
    publication_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
