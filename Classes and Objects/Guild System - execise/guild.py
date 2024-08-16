from Guild_System.player import Player


class Guild:
    def __init__(self, name):
        # """self.name == Guild Name"""
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        # """self.name == Guild Name"""
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            self.players.remove(player)
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = "\n".join([Player.player_info(pl_name) for pl_name in self.players])
        return f"Guild: {self.name}\n{players_info}"
