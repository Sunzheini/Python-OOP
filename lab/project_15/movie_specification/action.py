from project_15.movie_specification.movie import Movie


class Action(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

        self.likes = 0

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        result = f"Action - Title:{self.title}, Year:{self.year}, " \
                 f"Age restriction:{self.age_restriction}, " \
                 f"Likes:{self.likes}, " \
                 f"Owned by:{self.owner.username}"

        return result
