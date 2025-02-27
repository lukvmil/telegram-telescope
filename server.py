import uvicorn
from fastapi import FastAPI, Request

fastapi_app = FastAPI()

@fastapi_app.post("/telegram/listener")
async def telegram_listener(request: Request):
    print((await request.json()))

if __name__ == "__main__":
    uvicorn.run(
        "server:fastapi_app"
    )