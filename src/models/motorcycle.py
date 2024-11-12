from sqlalchemy import Column, Integer, String
from src.api.database import Base


class Motorcycle(Base):
    __tablename__ = "motorcycles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    identifier_code = Column(Integer, unique=True, index=True)
    license_plate = Column(String(10), unique=True, index=True)
    model = Column(String(50))
    year = Column(Integer)


    def __init__(self, identifier_code, license_plate, model, year):
        self.identifier_code = identifier_code
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