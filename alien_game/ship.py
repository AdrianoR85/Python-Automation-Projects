import pygame as pg

class Ship:

  def __init__(self, game):
    self.screen = game.screen
    self.game_settings = game.settings
    self.screen_rect = game.screen.get_rect()


    self.image = pg.image.load('assets/ship.bmp')
    self.rect = self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom

    self.x : float = float(self.rect.x)

    self.moving_right = False
    self.moving_left = False
  
  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.game_settings.ship_speed
    
    if self.moving_left and self.rect.left > 0:
      self.x -= self.game_settings.ship_speed
    
    self.rect.centerx = self.x # type: ignore

  def blitme(self):
    self.screen.blit(self.image, self.rect)
  
  