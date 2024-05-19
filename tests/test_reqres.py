import requests
from jsonschema import validate

from schemas import get_users, post_login, put_users, list_users, post_create, delayed_user

import json

url = "https://reqres.in/api/"


def test_post():
    response = requests.post(url + 'users', data={"first_name": "Emma", "last_name": "Wong"})
    body = response.json()
    assert response.status_code == 201
    assert body["first_name"] == "Emma"
    assert body["last_name"] == "Wong"
    with open('post_users.json') as file:
        schema = json.load(file)
    validate(body, schema=schema)


def test_get():
    response = requests.get(url + 'users', params={"page": 2, "per_page": 4},
                            data={"first_name": "Charles", "last_name": "Morris"})

    ids = [element['id'] for element in response.json()['data']]
    body = response.json()
    assert len(ids) == len(set(ids))
    assert response.status_code == 200
    validate(body, get_users)


def test_update():
    response = requests.put(url + "users/2")
    body = response.json()
    assert response.status_code == 200
    validate(body, put_users)


def test_delete():
    response = requests.delete(url + "users/2")
    assert response.status_code == 204
    assert response.text == ''


def test_unsuccessful():
    response = requests.post(url + 'login')
    body = response.json()
    assert response.status_code == 400
    validate(body, post_login)


def test_notfound():
    response = requests.get(url + 'unknown/23')
    assert response.status_code == 404
    assert response.text == '{}'


def test_patch_user():
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(url + 'users/2', data=payload)
    body = response.json()

    assert response.status_code == 200
    validate(body, put_users)
    assert body["name"] == "morpheus"
    assert body["job"] == "zion resident"


def test_list_user():
    response = requests.get(url + 'unknown')
    body = response.json()
    validate(body, list_users)
    assert body["per_page"] == 6
    assert body["page"] == 1


def test_create_user():
    response = requests.post(url + 'users')
    body = response.json()
    validate(body, post_create)
    assert body['id'] != 0


def test_delayed_responce():
    response = requests.get(url + 'users', params={"delay": 3, "page": 1, "per_page": 1, "total": 1})

    body = response.json()
    validate(body, delayed_user)
    assert body['data'] == [{"id": 1, "email":
        "george.bluth@reqres.in", "first_name": "George", "last_name":
                                 "Bluth", "avatar": "https://reqres.in/img/faces/1-image.jpg"}]
