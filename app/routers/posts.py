from fastapi import APIRouter


router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/get-posts")
async def get_posts():
    pass

@router.get("/get-post/{id}")
async def get_post(id: int):
    pass
