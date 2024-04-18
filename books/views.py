from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Book
from .forms import UserForm, BookForm, QueryForm, BookQueryForm
from django.forms import formset_factory


def home(request):
    ConstraintFormSet = formset_factory(QueryForm, extra=1)
    formset = ConstraintFormSet(request.POST or None)
    results = None
    users = User.objects.all()
    books = Book.objects.all()
    if request.method == 'POST' and formset.is_valid():
        results = User.objects.all()  # Initialize with all users if needed
        for form in formset:
            key = form.cleaned_data['key']
            constraint = form.cleaned_data['constraint']
            value = form.cleaned_data['value']
            results = results.filter(**{f'{key}__{constraint}': value})

    return render(request, 'books/home.html', {
        'formset': formset,
        'results': results,
        'users': users,
        'books': books
    })


def book_home(request):
    ConstraintFormSet_book = formset_factory(BookQueryForm, extra=1)
    formset_book = ConstraintFormSet_book(request.POST or None)
    results_book = None
    users = User.objects.all()
    books = Book.objects.all()
    print("hello")
    if request.method == 'POST' and formset_book.is_valid():
        results_book = Book.objects.all()
        for form in formset_book:
            key = form.cleaned_data['key']
            constraint = form.cleaned_data['constraint']
            value = form.cleaned_data['value']
            results_book = results_book.filter(
                **{f'{key}__{constraint}': value})
    return render(request, 'books/home.html', {
        'formset_book': formset_book,
        'results_book': results_book,
        'users': users,
        'books': books
    })


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


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('home')  # Redirect to the home page after deletion
    else:
        # If not POST, redirect to the confirmation page again or handle differently
        return redirect('books/confirm_delete', pk=pk)


def delete_confirmation(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'books/delete_confirmation.html', {'user': user})
