class Property:
    def __init__(self, address, city, status, price, year, description):
        self.address = address
        self.city = city
        self.status = status
        self.price = price
        self.year = year
        self.description = description

    def to_dict(self):
        return {
            "address": self.address,
            "city": self.city,
            "status": self.status,
            "price": self.price,
            "year": self.year,
            "description": self.description
        }
