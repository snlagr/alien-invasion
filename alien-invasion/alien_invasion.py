import sys
import pygame

def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	screen = pygame.display.set_mode((600,400))
	pygame.display.set_caption("Alien Invasion")

	# Start main loop of the game.
	while True:
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# make most recently drawn screen visible
		pygame.display.flip()

run_game()