import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.api.database import get_db, init_db, AsyncSessionLocal
from src.models.motorcycle import Motorcycle

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()   

@app.on_event("startup")
async def startup_event():
    async with AsyncSessionLocal() as session:
        motorcycle3 = Motorcycle(identifier_code = "5", license_plate="LAF 0974", model="Honda Fan", year= 2024)
        motorcycle4 = Motorcycle(identifier_code = "6", license_plate="MJH 0765", model="Yamaha Factor", year= 2020)

        session.add_all([motorcycle3, motorcycle4])
        await session.commit()

@app.get("/api/v1/health")
async def health_check():
    return JSONResponse(content={"status": "API is running"}, status_code=200)

@app.post("/api/v1/motorcycles")
async def add_motorcycle(identifier_code: int, licence_plate: str, model: str, year: int, db: AsyncSession = Depends(get_db)):
    new_motorcycle = Motorcycle(identifier_code, licence_plate, model, year)
    db.add(new_motorcycle)
    await db.commit()
    await db.refresh(new_motorcycle)
    return{"message": "Motorcycle added successfully"}

@app.get("/api/v1/motorcycles")
async def get_motorcycles(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Motorcycle))
    motorcycles = result.scalars().all()  
    return [motorcycle.__dict__ for motorcycle in motorcycles]

if __name__ == "__main__":
    uvicorn.run(app,port=8000)

