import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Enemies at the gates!"""

	def __init__(self, ai_settings, screen):
		"""Initialize and set starting pos"""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# load image and set its rectangle attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the alien's exact position
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw alien at its cureent location"""
		self.screen.blit(self.image, self.rect)