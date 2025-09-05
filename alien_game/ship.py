import pygame as pg

class Ship:
  def __init__(self, game):
    self.main_screen = game.screen

    self.image = pg.image.load("assets/ship.bmp")
    self.rect = self.image.get_rect()

    self.screen_rect = self.main_screen.get_rect()

    self.rect.midbottom = self.screen_rect.midbottom
  
  def draw_ship(self):
    self.main_screen.blit(self.image, self.rect)