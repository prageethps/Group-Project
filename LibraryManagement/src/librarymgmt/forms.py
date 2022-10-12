from django import forms
from .models import Books

class BooksCreateForm(forms.ModelForm):
   class Meta:
     model = Books
     fields = ['category', 'item_name', 'author', 'quantity', 'reserve_books']