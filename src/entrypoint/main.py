from fastapi import FastAPI,status
from src.crud.router.router import crud
from src.crud.router.blog_router import blog

app=FastAPI()
app.include_router(crud)
app.include_router(blog)


@app.get(path="/",status_code=status.HTTP_200_OK)
async def entry_point()->dict:
    return {"message":"Hello World","status":status.HTTP_200_OK}




    