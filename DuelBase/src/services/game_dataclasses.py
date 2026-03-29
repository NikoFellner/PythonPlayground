from dataclasses import dataclass


@dataclass
class FightResults:
    hero_alive: bool
    enemy_alive: bool
    hero_health:int
    enemy_health:int

@dataclass
class GameData:
    game_level: int =1