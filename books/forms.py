from django import forms
from .models import User, Book


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'liked_books']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price']


class QueryForm(forms.Form):

    KEY_CHOICES = [
        ('age', 'Age'),
        ('name', 'Name'),
        ('liked_books', 'Liked_books'),
    ]
    CONSTRAINT_CHOICES = [
        ('gt', 'Greater than'),
        ('lt', 'Less than'),
        ('exact', 'Equals'),

    ]

    key = forms.ChoiceField(choices=KEY_CHOICES)
    constraint = forms.ChoiceField(choices=CONSTRAINT_CHOICES)
    value = forms.CharField()


class BookQueryForm(forms.Form):

    KEY_CHOICES = [
        ('name', 'Name'),
        ('price', 'Price'),
    ]
    CONSTRAINT_CHOICES = [
        ('gt', 'Greater than'),
        ('lt', 'Less than'),
        ('exact', 'Equals'),

    ]

    key = forms.ChoiceField(choices=KEY_CHOICES)
    constraint = forms.ChoiceField(choices=CONSTRAINT_CHOICES)
    value = forms.CharField()
