from django.contrib import admin
from .forms import BooksCreateForm

# Register your models here.

from .models import Books

class BooksCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity', 'author', 'receive_books']
   form = BooksCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name', 'author', 'receive_books']

admin.site.register(Books, BooksCreateAdmin)