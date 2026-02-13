from Player import Player
from Enemy import Enemy
from Background import Background

class EntityFactory:
    @staticmethod
    def get_entity(entity_type: str):
        if entity_type == "Player":
            return Player("Player1", None, None) # Argumentos de exemplo
        elif entity_type == "Enemy":
            return Enemy("Enemy1", None, None)
        elif entity_type == "Background":
            return Background("Bg1", None, None)
        return None