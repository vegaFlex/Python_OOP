from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Customer


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        # customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        # dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return ('\n'.join([repr(x) for x in self.customers]) + '\n' +
                '\n'.join([repr(x) for x in self.dvds]))

    def __find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def __find_dvd_by_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
