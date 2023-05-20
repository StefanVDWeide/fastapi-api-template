from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_get_users(async_client: AsyncClient) -> None:
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

    rv = await async_client.get("users/get/users", headers=headers)
    assert rv.status_code == 200


@pytest.mark.anyio
async def test_get_user(async_client: AsyncClient) -> None:
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

    rv = await async_client.get("users/get/user/1", headers=headers)
    assert rv.status_code == 200


@pytest.mark.anyio
async def test_delete_user(async_client: AsyncClient) -> None:
    payload_register_user_one = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    await async_client.post("/auth/register", json=payload_register_user_one)

    payload_register_user_two = {
        "first_name": "string",
        "last_name": "string",
        "email": "user.two@example.com",
        "password": "string",
        "is_admin": False,
    }
    await async_client.post("/auth/register", json=payload_register_user_two)

    payload_login = {
        "username": "user@example.com",
        "password": "string",
    }
    r = await async_client.post("/auth/login", data=payload_login)
    r_json = r.json()
    headers = {"Authorization": f"Bearer {r_json['access_token']}"}

    rv = await async_client.delete("users/delete/user/2", headers=headers)
    assert rv.status_code == 200
