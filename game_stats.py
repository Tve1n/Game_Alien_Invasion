

class GameStats():
    """Отслеживания статисти игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
    
    def reset_stats(self):
        """Инициализирует статистику, изменяющихся в ходе игры."""
        self.ships_left = self.settings.ship_limit