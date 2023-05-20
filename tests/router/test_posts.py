from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_get_posts(async_client: AsyncClient) -> None:
    payload_register = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    await async_client.post("/auth/register", json=payload_register)

    payload_login = {
        "username": "user@example.com",
        "password": "string",
    }
    r = await async_client.post("/auth/login", data=payload_login)
    r_json = r.json()
    headers = {"Authorization": f"Bearer {r_json['access_token']}"}

    rv = await async_client.get("posts/get/posts", headers=headers)
    assert rv.status_code == 404


@pytest.mark.anyio
async def test_get_post(async_client: AsyncClient) -> None:
    payload_register = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    await async_client.post("/auth/register", json=payload_register)

    payload_login = {
        "username": "user@example.com",
        "password": "string",
    }
    r = await async_client.post("/auth/login", data=payload_login)
    r_json = r.json()
    headers = {"Authorization": f"Bearer {r_json['access_token']}"}

    rv = await async_client.get("posts/get/post/1", headers=headers)
    assert rv.status_code == 404


@pytest.mark.anyio
async def test_add_post(async_client: AsyncClient) -> None:
    payload_register = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    await async_client.post("/auth/register", json=payload_register)

    payload_login = {
        "username": "user@example.com",
        "password": "string",
    }
    r = await async_client.post("/auth/login", data=payload_login)
    r_json = r.json()
    headers = {"Authorization": f"Bearer {r_json['access_token']}"}

    payload_post = {"title": "string", "content": "string", "user_id": 1}

    rv = await async_client.post("posts/add/post", headers=headers, json=payload_post)
    assert rv.status_code == 200


@pytest.mark.anyio
async def test_delete_post(async_client: AsyncClient) -> None:
    payload_register = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    await async_client.post("/auth/register", json=payload_register)

    payload_login = {
        "username": "user@example.com",
        "password": "string",
    }
    r = await async_client.post("/auth/login", data=payload_login)
    r_json = r.json()
    headers = {"Authorization": f"Bearer {r_json['access_token']}"}

    payload_post = {"title": "string", "content": "string", "user_id": 1}

    await async_client.post("posts/add/post", headers=headers, json=payload_post)

    rv = await async_client.delete("/posts/delete/post/1", headers=headers)
    assert rv.status_code == 200
