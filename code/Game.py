from Level import Level

class Game:
    def __init__(self, window):
        self.window = window
        self.levels = [Level(window, "Fase 1")] # Composição: Game owns Levels

    def run(self):
        # Loop principal do jogo
        for level in self.levels:
            level.run()