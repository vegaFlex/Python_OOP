from project_2.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, curr_pokemon: Pokemon):
        if curr_pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(curr_pokemon)
        return f"Caught {curr_pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n'
        result += f'Pokemon count {len(self.pokemons)}\n'

        for pokemon in self.pokemons:
            result += f'- {pokemon.pokemon_details()}' + '\n'

        return result.strip()
