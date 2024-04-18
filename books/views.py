from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import User, Book
from .forms import UserForm, BookForm, QueryForm, BookQueryForm
from django.forms import formset_factory
from django.db.models import Count, Q


def home(request):
    users = User.objects.all()
    books = Book.objects.all()
    return render(request, 'books/home.html', {'users': users, 'books': books})


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=user)
    return render(request, 'books/user_detail.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_detail.html', {'form': form})


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'books/add_user.html', {'form': form})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def query_view(request):
    ConstraintFormSet = formset_factory(QueryForm, extra=1)
    formset = ConstraintFormSet(request.POST or None)
    results = None  # Start with all users
    if formset.is_valid():
        results = User.objects.all()
        for form in formset:
            key = form.cleaned_data['key']

            constraint = form.cleaned_data['constraint']

            value = form.cleaned_data['value']
            if key == 'liked_books':
                results = results.annotate(
                    num_liked_books=Count('liked_books'))
                results = results.filter(
                    **{f'num_liked_books__{constraint}': value})

            else:
                results = results.filter(**{f'{key}__{constraint}': value})
            print(results)
    return render(request, 'books/query.html', {'formset': formset,  'results': results})


def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('home')


def bookquery_view(request):
    ConstraintFormSet = formset_factory(BookQueryForm, extra=1)
    formset = ConstraintFormSet(request.POST or None)
    results = None  # Start with all users
    if formset.is_valid():
        results = Book.objects.all()
        for form in formset:
            key = form.cleaned_data['key']

            constraint = form.cleaned_data['constraint']

            value = form.cleaned_data['value']

            results = results.filter(**{f'{key}__{constraint}': value})

    return render(request, 'books/bookquery.html', {'formset': formset,  'results': results})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')
