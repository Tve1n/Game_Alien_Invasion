

class Settings():
    '''Класс для хранения настроек игры Alien Invasion'''

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 200)
        
        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 15
        self.bullet_height = 40
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 20
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        
        # fleet_direction = 1 Это движение вправо; а -1 это влево.
        self.fleet_direction = 1

        # Подсчёт очков
        self.alien_points = 50

    
    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        