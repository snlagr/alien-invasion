import sys
import pygame

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
	ship = Ship(screen)

	# Start main loop of the game.
	while True:
		# Watch for keyboard and mouse events
		gf.check_events()

		screen.fill(ai_settings.bg_color)
		ship.blitme()
		# make most recently drawn screen visible
		pygame.display.flip()

run_game()