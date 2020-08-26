import pytest
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_api.settings')
django.setup()

from books.models import Book


@pytest.fixture
def basic_book_data():
    return {
        "googleapis_id": "iY4yZEkphNgC",
        "title": "basic_book",
        "authors": "['basic author']",
        "published_date": "2015-04-02",
        "categories": "basic category",
        "thumbnail": "https://www.googleapis.com/books/v1/volumes/iY4yZEkphNgC"
    }


@pytest.fixture
def other_basic_book_data():
    return {
        "googleapis_id": "iY4yZasdhNgC",
        "title": "other_basic_book",
        "authors": "['John Smith']",
        "published_date": "2013",
        "categories": "basic category",
        "thumbnail": "https://www.googleapis.com/books/v1/volumes/iY4ysadphNgC"
    }


@pytest.fixture
def other_basic_book_with_the_same_published_date_data():
    return {
        "googleapis_id": "iY4yZEkphXXX",
        "title": "another basic book from 2015",
        "authors": "['basic author']",
        "published_date": "2015-02-05",
        "categories": "basic category",
        "thumbnail": "https://www.googleapis.com/books/v1/volumes/iY4yZEkphXXX"
    }


@pytest.fixture
def other_basic_book_with_2_authors_data():
    return {
        "googleapis_id": "iY4yZEkphcvb",
        "title": "basic book with 2 authors",
        "authors": "['basic author', 'John Smith']",
        "published_date": "2014-02-05",
        "categories": "basic category",
        "thumbnail": "https://www.googleapis.com/books/v1/volumes/iY4yZEkphXXX"
    }


@pytest.fixture()
def basic_book(db, basic_book_data):
    obj = Book(**basic_book_data)
    obj.save()
    yield obj
    obj.delete()


@pytest.fixture()
def other_basic_book(db, other_basic_book_data):
    obj = Book(**other_basic_book_data)
    obj.save()
    yield obj
    obj.delete()


@pytest.fixture()
def other_basic_book_with_the_same_published_date(db, other_basic_book_with_the_same_published_date_data):
    obj = Book(**other_basic_book_with_the_same_published_date_data)
    obj.save()
    yield obj
    obj.delete()


@pytest.fixture()
def other_basic_book_with_2_authors(db, other_basic_book_with_2_authors_data):
    obj = Book(**other_basic_book_with_2_authors_data)
    obj.save()
    yield obj
    obj.delete()