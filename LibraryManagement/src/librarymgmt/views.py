from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksCreateForm
# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	form = 'Welcome: This is the Home Page'
	context = {
		"title": title,
		"test": form,

	}
	return render(request, "home.html",context)

def list_item(request):
	title = 'List of Items'
	queryset = Books.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)

def add_items(request):
	form = BooksCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_item')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)