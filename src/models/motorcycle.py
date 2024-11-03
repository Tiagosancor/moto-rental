class Motorcycle:
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