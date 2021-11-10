from fastapi import FastAPI
import httpx
import os

app = FastAPI()
backend_addr = os.environ['COMPUTING_BK']

@app.get("/loads/matrixinverse")
async def read_item(msize: int):
    #print(f"Backend address: {backend_addr}")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{backend_addr}/loads/matrixinverse?msize={msize}", timeout=90.0)
        #print(f"Response: {response}")
    return response.json()

@app.get("/")
def read_root():
    return {"Front": "end"}
