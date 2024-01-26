from fastapi import APIRouter, status
from src.blog.service.service import BlogService

from src.blog.model.model import BlogPost, UpdateBlogPost

blog = APIRouter(prefix="/api/v1/blog", tags=["BLOG"])


@blog.get("/get", status_code=status.HTTP_200_OK)
async def blog_get(index: int):
    return BlogService().get(index=index)


@blog.get("/getall", status_code=status.HTTP_200_OK)
async def blog_getall():
    return BlogService().getall()


@blog.post("/add", status_code=status.HTTP_200_OK)
async def blog_getall(blog: BlogPost):
    return BlogService().add(data=blog)


@blog.delete("/delete", status_code=status.HTTP_200_OK)
async def blog_getall(index: int):
    return BlogService().delete(index=index)


@blog.put("/update", status_code=status.HTTP_200_OK)
async def blog_getall(index: int, data: UpdateBlogPost):
    updatePost = data.model_dump(exclude_unset=True)

    return BlogService().update(index=index, data=updatePost)
