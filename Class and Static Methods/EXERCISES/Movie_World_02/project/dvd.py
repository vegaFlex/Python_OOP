class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id, name, date, age_restriction):
        day, month, year = [int(x) for x in date.split('.')]
        creation_month = cls.get_month_name(month)
        return cls(name, dvd_id, year, creation_month, age_restriction)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})"
                f" has age restriction {self.age_restriction}. "
                f"Status: {'rented' if self.is_rented else 'not rented'}")

    @staticmethod
    def get_month_name(month: int) -> str:
        month_names = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]
        return month_names[month - 1]
