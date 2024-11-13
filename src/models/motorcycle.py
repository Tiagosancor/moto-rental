from sqlalchemy import Column, Integer, String
from src.api.database import Base


class Motorcycle(Base):
    __tablename__ = "motorcycles"

    identifier_code = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    license_plate = Column(String(10), unique=True, nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)


    def __init__(self, license_plate: str = "", model: str = "", year: int = 0):
        self.license_plate = license_plate  # Identificador único
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Motorcycle({self.identifier_code}, {self.license_plate}, {self.model}, {self.year})"


class MotorcycleRegistration:
    def __init__(self):
        self.motorcycles = []

    def add_motorcycles(self, motorcycle):
        self.motorcycles.append(motorcycle)

    def get_motocycles(self):
        return self.motorcycles