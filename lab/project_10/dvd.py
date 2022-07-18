from project_10.month_mapper import month_mapper


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        explode = date.split('.')
        creation_year, creation_month = int(explode[2]), int(explode[1])

        month_name = month_mapper[creation_month]

        return cls(name, id, creation_year, month_name, age_restriction)

    def __repr__(self):
        if not self.is_rented:
            status = "not rented"
        else:
            status = "rented"
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {status}"












