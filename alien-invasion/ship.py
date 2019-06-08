import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		"""Set ship's starting position."""
		self.screen = screen
		self.ai_settings = ai_settings

		# load ship.bmp and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start new ship at bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# store decimal value for ship's center
		self.center = float(self.rect.centerx)

		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update ships position based on movement flag."""
		# update ships center value, not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# update rect obect from self.center
		self.rect.centerx = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx