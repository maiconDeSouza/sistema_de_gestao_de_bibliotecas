from django import forms

from .models import Book, Author


class BookForms(forms.ModelForm):
    def __init__(self, *args, is_filter=False, **kwargs):
        super().__init__(*args, **kwargs)

        if is_filter:
            self.fields['author'].queryset = Author.objects.all()
            self.fields['author'].empty_label = "Todos"
        else:
            self.fields['author'].queryset = Author.objects.all()

    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    status = forms.ChoiceField(
        choices=[('', 'Todos')] + Book.STATUS_CHOICES, required=False)

    class Meta:
        model = Book
        fields = '__all__'
