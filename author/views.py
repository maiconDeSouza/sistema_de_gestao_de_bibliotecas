from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Author
from .forms import AuthorForms


class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForms
    template_name = 'author/pages/create_author.html'
    context_object_name = 'form'
    success_url = '/new/'
    login_url = '/account/login/'
