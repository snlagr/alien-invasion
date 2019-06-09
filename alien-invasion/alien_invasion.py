import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from button import Button

def run_game():
	
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# make a play button
	play_button = Button(ai_settings, screen, "Play")
	
	# create instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	# make ship, grpup of bullets and aliens	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Start main loop of the game.
	while True:
		# Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()