from EntityFactory import EntityFactory

class Level:
    def __init__(self):
        self.window = none
        self.name = none
        self.entity_list = []

    def run(self) -> None:
        # Lógica para atualizar e desenhar entidades no nível
        for entity in self.entity_list:
            entity.move()