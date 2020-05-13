from django.contrib import admin
from .models import Books

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'price')

admin.site.register(Books, BookAdmin)