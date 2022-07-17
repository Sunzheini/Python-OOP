class Album:
    def __init__(self, name, *songs):    # !!!
        self.name = name
        self.published = False
        self.songs = list(songs)         # !!!

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):

        for i in self.songs:
            if i.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                else:
                    self.songs.remove(i)
                    return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = ""

        result += f"Album {self.name}\n"
        for i in self.songs:
            result += f"== {i.get_info()}\n"

        return result.strip()
