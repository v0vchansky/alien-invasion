import pygame
from pygame.sprite import Sprite

class Alien(Sprite): # объект врагов

    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen  # экран
        self.settings=ai_game.settings # настройки экрана и общие нстаройки

        self.image=pygame.image.load('images/pngaaa.com-476369.bmp')
        self.rect=self.image.get_rect() # получаем размер картинки

        self.rect.x=self.rect.width # настраиваем хитбокс
        self.rect.y=self.rect.height

        self.x=float(self.rect.x) # позиция
    
    def update(self): # обновление позиции корабля
        #self.x+=self.settings.alien_speed
        self.x+=(self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x=self.x
    
    def check_edges(self): # проверка не подошел ли к грани экрана
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
        
