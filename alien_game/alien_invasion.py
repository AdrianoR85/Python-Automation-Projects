from settings import Settings
import pygame as pg
import sys

class AlienInvasion:
  def __init__(self) -> None:
    pg.init()
    self.settings = Settings()
    self.screen = pg.display.set_mode(
      (self.settings.screen_width, self.settings.screen_width)
    )
    self.clock = pg.time.Clock()

  def update(self):
    pg.display.flip() # Keep the most recent screen visible.
    self.clock.tick(self.settings.fps)
    pg.display.set_caption(f"Alien Invasion   FPS: {self.clock.get_fps() :.1f}")
  
  def draw_screen(self):
    self.screen.fill(self.settings.bg_color)

  def check_event(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.running = False
        pg.quit()
        sys.exit()

  def run_game(self):
    while True:
      self.check_event()
      self.update()

    

if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()