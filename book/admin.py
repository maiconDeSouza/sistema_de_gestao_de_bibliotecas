from django.contrib import admin

from .models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn',
                    'publication_date', 'status', 'created_at',)
    search_fields = ('title', 'author', 'isbn', 'status',)


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
