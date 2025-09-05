import sys
import pygame as pg

from settings import Settings
from ship import Ship
class AlienInvasion:

  def __init__(self) -> None:
    pg.init()
    self.clock = pg.time.Clock()
    self.settings = Settings()
    self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
    pg.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    

  def run_game(self):
    while True:
      for event in pg.event.get():
        if event.type == pg.QUIT:
          sys.exit()

      self.screen.fill(self.settings.bg_color)
      self.ship.draw_ship()
      pg.display.flip()
      self.clock.tick(self.settings.fps)


if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()