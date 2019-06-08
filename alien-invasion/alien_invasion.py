import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# make ship, grpup of bullets and aliens	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Start main loop of the game.
	while True:
		# Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship,
			aliens, bullets)

run_game()