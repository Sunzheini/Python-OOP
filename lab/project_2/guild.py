#from project_2.player import Player  # submitted
from Lab.project_2.player import Player   # working for me


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.DEFAULT_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):

        for i in self.players:
            if i.name == player_name:
                self.players.remove(i)
                i.guild = Player.DEFAULT_GUILD
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):

        result = f"Guild: {self.name}\n"

        for i in self.players:
            result += i.player_info() + '\n'

        return result.strip()









