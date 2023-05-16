from httpx import AsyncClient
import pytest


@pytest.mark.anyio
async def test_health(async_client: AsyncClient) -> None:
    rv = await async_client.get("/health")
    assert rv.status_code == 200
