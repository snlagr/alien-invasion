import pygame.font

class Scoreboard():
	"""A class to report scoring information."""

	def __init__(self, ai_setting, screen, stats):
		"""Initialise scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_setting = ai_setting
		self.stats = stats

		# font settings for scoring information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# prepare initial score image
		self.prep_score()

	def prep_score(self):
		"""Turn score into rendered image."""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

		# display score at top right of screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Draw score to screen."""
		self.screen.blit(self.score_image, self.score_rect)