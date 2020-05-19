from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Books
from django.contrib.auth.mixins import(
   LoginRequiredMixin,
   PermissionRequiredMixin,
)
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
# import json
from django.core import serializers



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

class SearchResultListView(View):

  def get(self, request, *args, **kwargs):
    search_text = request.GET.get('search_text')
    qs = filter_data(search_text)
    if request.is_ajax():
      print("AJAX request...")
      qs_json = serializers.serialize('json', qs)
      # result = []
      # for data in qs:
      #   result.append(data)
      # print(f"RESULT = {qs_json}")
      # return JsonResponse(qs, safe=False)
      # print(f"DATA===={qs_json}")
      return HttpResponse(qs_json, content_type='application/json')
    return render(request, 'books/search_result.html', {'books': qs})


def filter_data(text):
  if text != '' :
    qs = Books.objects.filter(
      Q(title__icontains=text) | Q(author__icontains=text)
      )
    return qs
  else:
    print("NONE OR EMPTY")
