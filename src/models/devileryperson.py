from sqlalchemy import Column, Integer, String, CHAR, Date
from datetime import date 
from src.api.database import Base
from sqlalchemy.orm import relationship

class DeliveryPerson(Base):
    __tablename__ = "deliverypersons"

    identifier_code = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    tax_id = Column(String(14), unique=True, nullable=False)
    license_number = Column(String(11), unique=True, nullable=False)
    license_category = Column(CHAR(2), nullable=False)
    license_image = Column(String(255), nullable=False)

    rentals = relationship("Rental", back_populates="deliveryperson")

    def __init__(self, name: str = "", birth_date: date = date.today(), tax_id: str = "", license_number: str = "", license_category: str = "", license_image: str = ""):
        self.name = name
        self.birth_date = birth_date
        self.tax_id = tax_id  # Identificador único
        self.license_number = license_number  # Identificador único
        self.license_category = license_category  # (A, B ou A+B)
        self.license_image = license_image  # Formato png, bmp

    def __repr__(self):
        return f"DeliveryPerson ({self.name}, {self.birth_date}, {self.tax_id}, {self.license_number}, {self.license_category}, {self.license_image})"
    
class DeliveryPersonRegistration:
    def __init__(self):
        self.deliverypersons = []

    def add_deliverypersons(self, deliveryperson):
        self.deliverypersons.append(deliveryperson)

    def get_deliverypersons(self):
        return self.deliverypersons
