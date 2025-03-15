from django import forms

from .models import Book, Author


class BookForms(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[('', 'Todos')] + Book.STATUS_CHOICES, required=False)

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Todos",
        required=False
    )

    class Meta:
        model = Book
        fields = '__all__'
