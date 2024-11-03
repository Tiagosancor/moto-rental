
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.models.motorcycle import Motorcycle, MotorcycleRegistration

app = FastAPI()

motorcycle_registry = MotorcycleRegistration()

motorcycle_registry.add_motorcycles(Motorcycle(identifier_code = 3, license_plate="LDF 0945", model="Honda Bis", year= 2024))
motorcycle_registry.add_motorcycles(Motorcycle(identifier_code = 12, license_plate="MGH 0945", model="Yamaha Neo", year= 2020))

@app.get("/api/v1/health")
async def health_check():
    return JSONResponse(content={"status": "API is running"}, status_code=200)

@app.post("/api/v1/motorcycles")
async def add_motorcycle(identifier_code: int, licence_plate: str, model: str, year: int):
    new_motorcycle = Motorcycle(identifier_code, licence_plate, model, year)
    motorcycle_registry.add_motorcycles(new_motorcycle)
    return{"message": "Motorcycle added successfully"}

@app.get("/api/v1/motorcycles")
async def get_motorcycles():
    motorcycles = motorcycle_registry.get_motocycles()      
    return JSONResponse (content=[motorcycle.__dict__ for motorcycle in motorcycles], status_code=200)

if __name__ == "__main__":
    uvicorn.run(app,port=8000)

