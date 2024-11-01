from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/v1/health")
async def health_check():
    return JSONResponse(content={"status": "API is running"}, status_code=200)


@app.get("/api/v1/motorcycles")
async def get_motorcycles():
    motorcycles = [
        {"id": 11, "model": "Honda Titan", "year": 2024},
        {"id": 15, "model": "Yamaha Neo 125", "year": 2022}
        ]
    return JSONResponse (content=motorcycles)