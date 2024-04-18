from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_book/', views.add_book, name='add_book'),
    path('query/', views.query_view, name='query_view'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('bookquery/', views.bookquery_view, name='bookquery_view'),
]
