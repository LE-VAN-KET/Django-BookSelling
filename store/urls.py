from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='index'),
    path('registration', views.registration, name='registration'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('book/<int:id>', views.get_book, name="book"),
    path('books', views.get_books, name="books"),
    path('category/<int:id>', views.get_book_category, name="category"),
    path('writer/<int:id>', views.get_writer, name="writer"),
]
