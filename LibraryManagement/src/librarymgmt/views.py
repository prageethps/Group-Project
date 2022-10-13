from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksCreateForm, BooksSearchForm
from django.contrib import messages
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
	form = BooksSearchForm(request.POST or None)
	queryset = Books.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}
	if request.method == 'POST':
		queryset = Books.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value(),
										author__icontains=form['author'].value(),
										reserve_books__icontains=form['reserve_books'].value(),
										)
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
}

	return render(request, "list_item.html", context)

def add_items(request):
	form = BooksCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Saved')
		return redirect('/list_item')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_items.html", context)