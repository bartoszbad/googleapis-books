import pytest
from json import dumps, loads
from django.forms.models import model_to_dict
from rest_framework import status

BOOKS_ENDPOINT = "/books"


def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


def test_get_book_list(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date
):
    response = client.get(BOOKS_ENDPOINT)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


def test_get_book_list_sorted_descending(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date
):
    url = f"{BOOKS_ENDPOINT}?sort=-published_date"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    result = to_dict(response.data)
    assert result[0] == model_to_dict(basic_book)
    assert result[1] == model_to_dict(other_basic_book_with_the_same_published_date)
    assert result[2] == model_to_dict(other_basic_book)


def test_get_book_list_sorted_ascending(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date
):
    url = f"{BOOKS_ENDPOINT}?sort=published_date"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    result = to_dict(response.data)
    assert result[0] == model_to_dict(other_basic_book)
    assert result[1] == model_to_dict(other_basic_book_with_the_same_published_date)
    assert result[2] == model_to_dict(basic_book)


def test_get_book_list_filtered_by_author(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date,
    other_basic_book_with_2_authors
):
    url = f"{BOOKS_ENDPOINT}?author='basic author'"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3


def test_get_book_list_filtered_by_year(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date,
    other_basic_book_with_2_authors
):
    url = f"{BOOKS_ENDPOINT}?published_date=2015"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    print(response.data)
    assert len(response.data) == 2


def test_get_book_list_filtered_by_authors(
    db, client, basic_book, other_basic_book,
    other_basic_book_with_the_same_published_date,
    other_basic_book_with_2_authors
):
    url = f"{BOOKS_ENDPOINT}?author='basic author'&author='John Smith'"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    print(response.data)
    assert len(response.data) == 2



