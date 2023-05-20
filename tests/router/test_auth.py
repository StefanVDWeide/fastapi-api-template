from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_register(async_client: AsyncClient) -> None:
    payload = {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "password": "string",
        "is_admin": True,
    }
    rv = await async_client.post("/auth/register", json=payload)
    assert rv.status_code == 200


@pytest.mark.anyio
async def test_login(async_client: AsyncClient) -> None:
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
    rv = await async_client.post("/auth/login", data=payload_login)
    assert rv.status_code == 200
