import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    self.settings = Settings()

    self.screen = pg.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height)
    )
    pg.display.set_caption(f"Alien Invasion")
  
    self.ship = Ship(self)
    self.bullets = pg.sprite.Group()

  def run_game(self):
    while True:
      self._check_event()
      self.ship.update()
      self._update_bullet()
      self._update_screen()
      self.clock.tick(self.settings.fps)


  def _update_bullet(self):
    self.bullets.update() 

    for bullet in self.bullets.copy():
      if bullet.rect.bottom <=0:
        self.bullets.remove(bullet)

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.ship.blitme()
    
    pg.display.flip() # Keep the most recent screen visible.

  def _check_event(self,):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()
      elif event.type == pg.KEYDOWN:
        self._check_keydown_event(event)
      elif event.type == pg.KEYUP:
        self._check_keyup_event(event)
      
  def _check_keydown_event(self, event):
    if event.key == pg.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pg.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pg.K_SPACE:
      self._fire_bullet()

  def _check_keyup_event(self, event):
    if event.key == pg.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pg.K_LEFT:
      self.ship.moving_left = False
  
  def _fire_bullet(self):
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()