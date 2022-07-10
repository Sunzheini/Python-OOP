from Lab.project_2.pokemon import Pokemon
#from project_2.pokemon import Pokemon    # submitted with this


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for i in self.pokemons:
            if i.name == pokemon_name:
                self.pokemons.remove(i)
                return f"You have released {i.name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for j in self.pokemons:
            result += f"- {j.pokemon_details()}\n"

        return result.strip()















