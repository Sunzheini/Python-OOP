from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(hr.race_type == race_type for hr in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")
        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

# ------------------------------------------------------------------------------------------------

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        wanted_jockey = self.find_object_by_name(jockey_name, self.jockeys)
        if wanted_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse_index in range(len(self.horses)-1, -1, -1):
            if self.horses[horse_index].__class__.__name__ == horse_type and not self.horses[horse_index].is_taken:
                if wanted_jockey.horse is not None:
                    return f"Jockey {jockey_name} already has a horse."

                wanted_jockey.horse = self.horses[horse_index]
                self.horses[horse_index].is_taken = True
                return f"Jockey {jockey_name} will ride the horse {self.horses[horse_index].name}."

        raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        wanted_jockey = self.find_object_by_name(jockey_name, self.jockeys)
        if wanted_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for hr in self.horse_races:
            if hr.race_type == race_type:
                if wanted_jockey.horse is None:
                    raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
                if wanted_jockey in hr.jockeys:
                    return f"Jockey {jockey_name} has been already added to the {race_type} race."
                hr.jockeys.append(wanted_jockey)
                return f"Jockey {jockey_name} added to the {race_type} race."

        raise Exception(f"Race {race_type} could not be found!")

    def start_horse_race(self, race_type: str):
        wanted_hr = self.find_object_by_type(race_type, self.horse_races)
        if wanted_hr is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(wanted_hr.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        horse_name = ''
        winner = ''
        for participant in wanted_hr.jockeys:
            horse_used_object = participant.horse
            horse_speed = horse_used_object.speed
            if horse_speed > highest_speed:
                highest_speed = horse_speed
                horse_name = horse_used_object.name
                winner = participant

        return f"The winner of the {race_type} race, " \
               f"with a speed of {highest_speed}km/h is " \
               f"{winner.name}! Winner's horse: {horse_name}."

# ------------------------------------------------------------------------------------------------

    @staticmethod
    def find_object_by_name(name, collection):
        for i in collection:
            if i.name == name:
                return i
        return None

    @staticmethod
    def find_object_by_type(name, collection):
        for i in collection:
            if i.race_type == name:
                return i
        return None



