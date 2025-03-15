from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View

from .models import Book


# Create your views here.

class ListBooks(ListView):
    model = Book
    template_name = 'book/pages/index.html'
    context_object_name = 'books'


class ChangeStatus(View):
    def get(self, request, pk, status):
        book = get_object_or_404(Book, pk=pk)
        book.status = status
        book.save()

        return redirect('index')
