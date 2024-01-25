from fastapi import APIRouter,status
from src.crud.service.blog_services import BlogService

from src.crud.model.blog import BlogPost

blog=APIRouter(prefix="/api/v1/blog",tags=["BLOG"])

@blog.get("/get",status_code=status.HTTP_200_OK)
async def blog_get(index:int):
    
    return BlogService().get(index=index)
@blog.get("/getall",status_code=status.HTTP_200_OK)
async def blog_getall():
    
    return BlogService().getall()
@blog.post("/add",status_code=status.HTTP_200_OK)
async def blog_getall(blog:BlogPost):
    
    return BlogService().add(data=blog)



