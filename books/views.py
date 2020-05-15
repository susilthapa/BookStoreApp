from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Books

from django.contrib.auth.mixins import(
   LoginRequiredMixin,
   PermissionRequiredMixin,
)

class BookListView(LoginRequiredMixin, ListView):
  model = Books
  context_object_name = 'books'
  template_name = 'books/book_list.html'
  login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
  model = Books
  context_object_name = 'book'
  template_name = 'books/book_detail.html'
  login_url = 'account_login'
  permission_required = 'books.special_status'
