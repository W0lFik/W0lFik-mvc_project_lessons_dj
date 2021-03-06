# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from app.books.models import Book
from app.books.forms import BookForm
from .filters import BookFilter


def get_books_list(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            book_desc = form.cleaned_data['description']
            authors = form.cleaned_data['author']

    form = BookForm()
    books = Book.objects.all()
    # books =
    # /?qwerty=12&asd=34
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        # 'books':books,
        'filter': filter,
        'form': form
    }
    return render(request, 'books/book_list.html', context=context)


class BookList(ListView):
    model = Book
    context_object_name = 'books'


class BooksDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'pk'












# def get_books_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books,
#     }
#
#     return render(request, 'books/all_books.html', context)

# queryset = Book.objects.all()
# template_name = 'book_list.html'
# model = Book
# context_object_name = 'books'
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['books'] = self.queryset
#     context['title'] = 'городская библиотека'
#     return context


# template_name = 'book_detail.html'
# queryset = Book.objects.all()
#
# def get_object(self, pk):
#     book = Book.objects.get(pk=pk)
#     return book
# template_name = 'books_detail.html'
# print('ww')


# def get_book(request, id_book):
#     books = Book.objects.get(pk=id_book)
#     return books

#
# def get_books_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books,
#     }
#
#     return render(request, 'books/all_books.html', context)

# генерация шаблона
# books = Book.objects.all()
#
# context = {
#     'books': books,
#     'sale': True,}

# return HttpResponse(f"<h1>{gets_book}</h1>")

# m_book = Book.objects.get()
# m_book = Book.objects.get(id_publishing_house__pub_house_name="Издательство 3")
# print(m_book.book_name)
# # m_book = Book.objects.all().first()
# pub_query = PublishingHouse.objects.all()
# author_query = Author.objects.filter(pk=1).prefetch_related('books')
# for i in pub_query:
#     pubg = i
#
# for j in author_query:
#     author = i
# books = author.book.first()
# print(books)

# author_query = Author.objects.filter(pk=1).prefetch_related('books')
# for a in author_query:
#     author = a
# context = {
#     "author": author,
# }

# pub_query = PublishingHouse.objects.prefetch_related('publishinghouse_books').all()

# for pub_house in pub_query:
#     for book in pub_house.publishinghouse_books.all():
#         print(book.book_name)
#

# pub_query = PublishingHouse.objects.values(
#     'pub_house_name',
#     'pub_house_site'
# )

# pub_query = PublishingHouse.objects.exclude(
#     is_daleted=False,
# )
# for pub_house in pub_query:
#     publisher = pub_house
#     print(publisher)
#
# return HttpResponse(f"<h1>{publisher}</h1>")

# author_list = (
#     Author(first_name="имя1",last_name='фам1' ,country='Россия' ,birthday="2002-01-02"),
#     Author(first_name="имя2", last_name='фам2', country='Россия', birthday="2002-01-02"),
#     )
# Author.objects.bulk_create(
#     author_list
# )
# return HttpResponse(f"<h1>ok</h1>")

# def get_books_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books,
#     }
