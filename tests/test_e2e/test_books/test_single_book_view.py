import pytest
from json import dumps, loads
from rest_framework import status

SINGLE_BOOK_ENDPOINT = "/books/"


def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


def test_get_existing_book(db, client, basic_book):
    url = f"{SINGLE_BOOK_ENDPOINT}{basic_book.id}"
    expected_response = [{
        "id": basic_book.id,
        "googleapis_id": basic_book.googleapis_id,
        "title": basic_book.title,
        "authors": basic_book.authors,
        "published_date": basic_book.published_date,
        "categories": basic_book.categories,
        "thumbnail": basic_book.thumbnail
    }]
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    result = to_dict(response.data)
    assert result == expected_response


def test_get_not_existing_book(db, client, basic_book):
    url = f"{SINGLE_BOOK_ENDPOINT}999"
    response = client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND