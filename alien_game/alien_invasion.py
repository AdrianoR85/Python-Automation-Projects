import sys
import pygame as pg

from settings import Settings
from ship import Ship

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

  def run_game(self):
    while True:
      self._check_event()
      self._update()
      self.clock.tick(self.settings.fps)

  def _update(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    pg.display.flip() # Keep the most recent screen visible.
    
  def _check_event(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()


if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()