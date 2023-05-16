from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/get-users")
async def get_users():
    pass

@router.get("/get-user/{id}")
async def get_user(id: int):
    pass
