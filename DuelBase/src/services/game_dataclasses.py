from dataclasses import dataclass


@dataclass
class FightResults:
    hero_alive: bool
    enemy_alive: bool
    hero_health:int
    enemy_health:int

@dataclass
class GameData:
    game_level:int = 1

@dataclass
class GameSummary:
    final_hero_health:int
    levels_cleard: int =1
    hero_alive:bool = True