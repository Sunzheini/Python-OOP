class Customer:
    ID = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    @staticmethod           # !!!
    def get_next_id():
        result = Customer.ID
        Customer.ID += 1
        return result

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; " \
               f"Email: {self.email}"









