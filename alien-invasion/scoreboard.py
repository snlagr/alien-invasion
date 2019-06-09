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

		# prepare initial score images
		self.prep_score()
		self.prep_high_score()

	def prep_score(self):
		"""Turn score into rendered image."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)

		# display score at top right of screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Turn high score into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_setting.bg_color)

		# center high score at top of screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def show_score(self):
		"""Draw score to screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)