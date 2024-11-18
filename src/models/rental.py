from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from datetime import date
from src.api.database import Base
from sqlalchemy.orm import relationship

class Rental(Base):
    __tablename__ = "rentals"

    identifier = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    start_date = Column(Date, nullable=False) 
    end_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    expected_end_date = Column(Date, nullable=True)
    additional_fee = Column(Float, nullable=True)
    penalty_percentage = Column(Float, nullable=True)
    total_amount = Column(Float, nullable=True)
    deliveryperson_id = Column(Integer, ForeignKey("deliverypersons.identifier_code"), nullable=True)
    plan_id = Column(Integer, ForeignKey("plans.identifier"), nullable=True)

    deliveryperson = relationship("DeliveryPerson", back_populates="rentals")
    plan = relationship("Plan", back_populates="rentals")
    motorcycles = relationship("Motorcycle", back_populates="rental")

    def __init__(self, start_date: date = date.today(), end_date: date = date.today(), return_date: date = date.today(),
                expected_end_date: date = date.today(), additional_fee: float = 0.0, penalty_percentage: float = 0.0, total_amount: float = 0.0, deliveryperson_id: int = 0, plan_id: int = 0): 
        self.start_date = start_date
        self.end_date = end_date
        self.return_date = return_date
        self.expected_end_date = expected_end_date
        self.additional_fee = additional_fee
        self.penalty_percentage = penalty_percentage
        self.total_amount = total_amount
        self.deliveryperson_id = deliveryperson_id
        self.plan_id = plan_id

    def __repr__(self):
        return f"Rental({self.start_date}, {self.end_date}, {self.return_date}, {self.expected_end_date},  {self.additional_fee},  {self.penalty_percentage},  {self.total_amount})"
    

class RentalRegistration:
    def __init__(self):
        self.rentals = []

    def add_rentals(self, rental):
        self.rentals.append(rental)

    def get_rentals(self):
        return self.rentals