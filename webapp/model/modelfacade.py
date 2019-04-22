import universe
import player as ply


class Facade:
    def __init__(self):
        self.universe = universe.Universe();
        self.player = None

    def create_player(self, name, prefDifficulty, skillPoints, location):
        if self.player is None:
            self.player = ply.Player(name, prefDifficulty, skillPoints, location)
        else:
            self.player.name = name
            self.player.prefDifficulty = prefDifficulty
            self.player.skills = skillPoints
            self.player.location = location


def get_instance():
    return Facade()
