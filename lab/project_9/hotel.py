class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([i.guests for i in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [i for i in self.rooms if i.number == room_number][0]    # !!!
        return room.take_room(people)

    def free_room(self, room_number):
        room = [i for i in self.rooms if i.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [str(i.number) for i in self.rooms if not i.is_taken]
        taken_rooms = [str(i.number) for i in self.rooms if i.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"



