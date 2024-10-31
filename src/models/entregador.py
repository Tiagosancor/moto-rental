class DeliveryPerson:
    def __init__(self, identifier_code, name, birth_date, tax_id, license_number, license_category, license_image):
        self.identifier_code = identifier_code
        self.name = name
        self.birth_date = birth_date
        self.tax_id = tax_id  # Identificador único
        self.license_number = license_number  # Identificador único
        self.license_category = license_category  # (A, B ou A+B)
        self.license_image = license_image  # Formato png, bmp
