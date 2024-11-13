import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.api.database import get_db, init_db, AsyncSessionLocal
from src.models.motorcycle import Motorcycle

app = FastAPI()



@app.on_event("startup")
async def startup_event():
    await init_db() 


    async with AsyncSessionLocal() as session:
        motorcycle11 = Motorcycle(license_plate="LAF 0974", model="Honda Fan", year= 2024)
        motorcycle12 = Motorcycle(license_plate="MJH 0765", model="Yamaha Factor", year= 2020)

        session.add_all([motorcycle11, motorcycle12])
        await session.commit()

@app.get("/api/v1/health")
async def health_check():
    return JSONResponse(content={"status": "API is running"}, status_code=200)

@app.post("/api/v1/motorcycles")
async def add_motorcycle(license_plate: str, model: str, year: int, db: AsyncSession = Depends(get_db)):
    new_motorcycle = Motorcycle(license_plate=license_plate, model=model, year=year)
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

