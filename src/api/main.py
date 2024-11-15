import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.api.database import get_db, init_db
from src.models.motorcycle import Motorcycle
from src.models.rental import Rental
from src.models.devileryperson import DeliveryPerson
from src.models.plan import Plan
from fastapi.responses import RedirectResponse
from datetime import date

app = FastAPI()



@app.on_event("startup")
async def startup_event():
    await init_db() 

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

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

@app.post("/api/v1/rentals")
async def add_rental(start_date: date, end_date: date, return_date: date, expected_end_date: date, 
                     additional_fee: float, penalty_percentage: float, total_amount: float, db: AsyncSession = Depends(get_db)):
    new_rental = Rental(start_date=start_date, end_date=end_date, return_date=return_date, expected_end_date=expected_end_date,
                         additional_fee=additional_fee, penalty_percentage=penalty_percentage, total_amount=total_amount)
    db.add(new_rental)
    await db.commit()
    await db.refresh(new_rental)
    return{"message": "Rental added successfully"}

@app.get("/api/v1/rentals")
async def get_rentals(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Rental))
    rentals = result.scalars().all()
    return [rental.__dict__ for rental in rentals]

@app.post("/api/v1/deliverypersons")
async def add_deliveryperson(name: str, birth_date: date, tax_id: str, license_number: str, license_category: str, license_image: str, db: AsyncSession = Depends(get_db)):
    new_deliveryperson = DeliveryPerson(name=name, birth_date=birth_date, tax_id=tax_id, license_number=license_number, license_category=license_category, license_image=license_image)
    db.add(new_deliveryperson)
    await db.commit()
    await db.refresh(new_deliveryperson)
    return{"message": "DeliveryPerson added successfully"}

@app.get("/api/v1/deliverypersons")
async def get_deliverypersons(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(DeliveryPerson))
    deliverypersons = result.scalars().all()
    return [deliveryperson.__dict__ for deliveryperson in deliverypersons]

@app.post("/api/v1/plans")
async def add_plan(description: str, daily_rate: float, days_quantity: int, db: AsyncSession = Depends(get_db)):
    new_plan = Plan(description=description, daily_rate=daily_rate, days_quantity=days_quantity)
    db.add(new_plan)
    await db.commit()
    await db.refresh(new_plan)
    return{"message": "Plan added successfully"}
 
@app.get("/api/v1/plans")
async def get_plans(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Plan))
    plans = result.scalars().all()
    return [plan.__dict__ for plan in plans]

if __name__ == "__main__":
    uvicorn.run(app,port=8000)

