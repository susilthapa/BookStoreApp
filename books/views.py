from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Books

from django.contrib.auth.mixins import(
   LoginRequiredMixin,
   PermissionRequiredMixin,
)
from django.http import HttpResponse

class BookListView(LoginRequiredMixin, ListView):
  model = Books
  context_object_name = 'books'
  template_name = 'books/book_list.html'
  login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
  model = Books
  context_object_name = 'book'
  template_name = 'books/book_detail.html'
  login_url = 'account_login'
  permission_required = 'books.special_status'
  permission_denied_message = 'SORRY! You dont have the permission!'

  def handle_no_permission(self):
    if self.request.user.has_perm('books/book_detail.html') == False:
      return HttpResponse(f"<h1>{self.permission_denied_message}</h1>")
