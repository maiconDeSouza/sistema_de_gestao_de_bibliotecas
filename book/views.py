from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic import ListView
from django.views import View

from .models import Book
from .forms import BookForms


# Create your views here.

class ListBooks(ListView):
    model = Book
    template_name = 'book/pages/index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookForms()
        return context


class FilterBooks(View):
    def get(self, request):
        pk_author = request.GET.get('author')
        status = request.GET.get('status')
        books, available_authors = Book.objects.filter_book(pk_author, status)
        books = get_list_or_404(books)
        form = BookForms(initial={'author': pk_author, 'status': status})
        form.fields['author'].queryset = available_authors
        return render(request, 'book/pages/index.html', {'books': books, 'form': form})


class SearchBooks(View):
    def get(self, request):
        search = request.GET.get('q')
        books = Book.objects.search_title_isbn(search)
        form = BookForms()

        return render(request, 'book/pages/index.html', {'books': books, 'form': form})


class ChangeStatus(View):
    def get(self, request, pk, status):
        book = get_object_or_404(Book, pk=pk)
        book.status = status
        book.save()

        return redirect('index')
