import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
    self.aliens = pg.sprite.Group()

    self._create_fleet()

  def run_game(self):
    while True:
      self._check_event()
      self.ship.update()
      self._update_bullet()
      self._update_alien()
      self._update_screen()
      self.clock.tick(self.settings.fps)


  def _update_bullet(self):
    self.bullets.update() 

    for bullet in self.bullets.copy():
      if bullet.rect.bottom <=0:
        self.bullets.remove(bullet)
  
  def _update_alien(self):
    """Update the positions of all aliens in the fleet."""
    """Check if the fleet is at an edge, then update positions."""
    self._check_fleet_edges()
    self.aliens.update()

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.ship.draw_ship()
    self.aliens.draw(self.screen)

    pg.display.flip() # Keep the most recent screen visible
  

  def _create_fleet(self):
    # Create an alien and keep adding aliens until there's no room left.
    # Spacing between aliens is one alien width and one alien height.
    alien = Alien(self)
    self.aliens.add(alien)

    alien_x, alien_y = alien.rect.size
    current_x, current_y = alien_x, alien_y
    while current_y < (self.settings.screen_height - 3 * alien_y):
      while current_x < (self.settings.screen_width - 2 * alien_x):
        self._create_alien(current_x, current_y)
        current_x += 2 * alien_x
      
      # Finished a row; reset x value, and increment y value.
      current_x = alien_x
      current_y += 2 * alien_y
  
  def _create_alien(self, x_pos, y_pos):
    new_alien = Alien(self)
    new_alien.x = x_pos
    new_alien.rect.x = x_pos
    new_alien.rect.y = y_pos
    self.aliens.add(new_alien)


  def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1


  def _check_fleet_edges(self):
    """ Respond appropriately if any alien have reach an edge"""
    for alien in self.aliens.sprites():
      if alien.check_edges():
        self._change_fleet_direction()
        break

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
    elif event.key == pg.K_q:
      sys.exit()

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