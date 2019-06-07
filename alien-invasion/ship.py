import pygame

class Ship():
	def __init__(self, screen):
		"""Set ship's starting position."""
		self.screen = screen

		# load ship.bmp and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start new ship at bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update ships position based on movement flag."""
		if self.moving_right:
			self.rect.centerx += 1
		if self.moving_left:
			self.rect.centerx -= 1

	def blitme(self):
		self.screen.blit(self.image, self.rect)