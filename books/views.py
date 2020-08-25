import requests
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from books.models import Book
from books.serializers import AddSetSerializer, BookSerializer


class AddSetToDBView(generics.CreateAPIView):
    """
    View which allow post request with body in format {"q": param}
    Next immediately send get request to https://www.googleapis.com/books/v1/volumes?q={param}
    Finally it saves request from googleapis to application data base
    """
    permission_classes = (AllowAny,)
    serializer_class = AddSetSerializer

    def post(self, request):
        url = f"https://www.googleapis.com/books/v1/volumes?q={request.data['q']}"
        r = requests.get(url=url)
        books_raw = r.json()
        try:
            books = books_raw["items"]
        except KeyError:
            return Response(status=status.HTTP_204_NO_CONTENT)

        for book in books:
            title = book["volumeInfo"].get("title", None)
            authors = book["volumeInfo"].get("authors", None)
            published_date = book["volumeInfo"].get("publishedDate", None)
            categories = book["volumeInfo"].get("categories", None),
            thumbnail = book["volumeInfo"].get("imageLinks", {}).get("thumbnail", None)

            if Book.objects.filter(googleapis_id=book["id"]).exists():
                existing_book = Book.objects.filter(googleapis_id=book["id"])
                existing_book.title = title
                existing_book.authors = authors
                existing_book.published_date = published_date
                existing_book.categories = categories
                existing_book.thumbnail = thumbnail
            else:
                Book.objects.create(
                    googleapis_id=book["id"],
                    title=title,
                    authors=authors,
                    published_date=published_date,
                    categories=categories,
                    thumbnail=thumbnail
                )

        return Response(status=status.HTTP_201_CREATED)


class ListBooksView(generics.ListAPIView):
    """
    List all books from application database
    Accepts params: sort, author, published_date
    """
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all()
        qp = self.request.query_params
        keys = qp.keys()

        # Filter by published date if published_date in params
        if "published_date" in keys:
            queryset = queryset.filter(published_date__contains=qp["published_date"])

        # Filter by authors if author in params
        if "author" in keys:
            queryset = queryset.filter(authors__contains=qp["author"])

        # Sort by published day if sort in params
        if "sort" in keys:
            queryset = queryset.order_by(qp["sort"])

        return queryset


class SingleBookView(generics.ListAPIView):
    """
    Show requested book by pk provided in URL
    """
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        book = Book.objects.filter(id=self.kwargs.get("pk"))
        if book:
            return book
        else:
            raise NotFound
