import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):

  def __init__(self, game) -> None:
    super().__init__()
    self.screen = game.screen
    self.settings = game.settings
    self.color = self.settings.buller_color

    # Create a bullet rect at (0, 0) and then set correct position.
    self.rect = pg.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
    self.rect.midtop = game.ship.rect.midtop

    self.y = float(self.rect.y)
  
  def update(self):
    self.y -= self.settings.bullet_speed
    self.rect.y = self.y

  def draw_bullet(self):
    pg.draw.rect(self.screen, self.color, self.rect)


