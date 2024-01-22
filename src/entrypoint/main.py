from fastapi import FastAPI,status
from src.crud.router.router import crud

app=FastAPI()
app.include_router(crud)

@app.get(path="/",status_code=status.HTTP_200_OK)
async def entry_point()->dict:
    return {"message":"Hello World","status":status.HTTP_200_OK}
    