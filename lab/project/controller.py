from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return

        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        
        idx, supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        heal = supply.energy
        player.stamina += heal
        if player.stamina > Player.MAX_STAMINA:
            player.stamina = Player.MAX_STAMINA

        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self.__find_player_by_name(first_player_name)
        player_2 = self.__find_player_by_name(second_player_name)

        error_message = ''
        if player_1.stamina == 0:
            error_message += f"Player {player_1.name} does not have enough stamina."
        if player_2.stamina == 0:
            error_message += '\n' + f"Player {player_2.name} does not have enough stamina."
        if error_message:
            return error_message.strip()

        if player_2.stamina < player_1.stamina:
            player_1, player_2 = player_2, player_1

        player_2.stamina -= player_1.stamina / 2
        if player_2.stamina < 0:
            player_2.stamina = 0

        if player_2.stamina == 0:
            return f"Winner: {player_1.name}"

        player_1.stamina -= player_2.stamina / 2
        if player_1.stamina < 0:
            player_1.stamina = 0

        if player_1.stamina == 0:
            return f"Winner: {player_2.name}"

        winner = player_1 if player_1.stamina > player_2.stamina else player_2
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()

    def __find_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for i in range(len(self.supplies)-1, -1, -1):
            current_supply = self.supplies[i]
            if current_supply.__class__.__name__ == sustenance_type:
                return i, current_supply
        return -1, None



