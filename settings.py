class Settings():
    def __init__(self):
        self.screen_width=1280
        self.screen_height=800
        self.bg_colour=(210,230,230)
        #параметр корабля
        self.ship_limit=3 # кол-во жизней
        #параметр пришельца
        self.fleet_drop_speed=5 # с какоц скоростью падают карабли
        #ПАРАМЕТР СНАРЯДА
        self.bullet_width=5  #Ширина пули
        self.bullet_height=15
        self.bullet_color=(50,50,20)
        self.bullet_allowed=5
        #Темп ускорения игры
        self.speed_scale=1.001
        self.score_scale=1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=1.0
        self.alien_score=50
        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed*=self.speed_scale
        self.bullet_speed*=self.speed_scale
        self.alien_speed*=self.speed_scale
        self.alien_score*=self.score_scale
