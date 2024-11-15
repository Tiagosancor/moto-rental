from sqlalchemy import Column, Integer, String, Float
from src.api.database import Base

class Plan(Base):
    __tablename__ = "plans"

    identifier = Column(Integer, primary_key=True, unique=True, nullable=False)
    decription = Column(String(50), nullable=False)
    daily_rate = Column(Float, nullable=False)
    days_quantity = Column(Integer, nullable=False)

    def __init__(self, description: str = "", daily_rate: float = 0.0, days_quantity: int = 0):
        self.description = description 
        self.daily_rate = daily_rate
        self.days_quantity = days_quantity

    def __repr__(self):
        return f"({self.identifier} ,{self.decription}, {self.daily_rate}, {self.days_quantity})"
    

class PlanRegistration:
    def __init__(self):
        self.plans = []

    def add_plans(self, plan):
        self.plans.append(plan)

    def get_plans(self):
        return self.plans


