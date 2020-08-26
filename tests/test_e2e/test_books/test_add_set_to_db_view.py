import pytest
from json import dumps
from rest_framework import status

from books.models import Book

URL = "/db"


def test_post_not_existing_body(db, client):
    body = {"q": "dddddddddddóba"}
    response = client.post(URL, dumps(body), content_type="application/json")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_post_existing_body_save_to_db(db, client):
    body = {"q": "Hobbit"}
    response = client.post(URL, dumps(body), content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(Book.objects.all()) == 10


def test_post_existing_body_update_db(db, client):
    body = {"q": "Hobbit"}
    response = client.post(URL, dumps(body), content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    assert len(Book.objects.all()) == 10
    response2 = client.post(URL, dumps(body), content_type="application/json")
    assert response2.status_code == status.HTTP_201_CREATED
    assert len(Book.objects.all()) == 10