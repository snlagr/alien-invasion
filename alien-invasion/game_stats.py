class GameStats():
	"""Track various statistics"""

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.game_active = False
		self.reset_stats()

	def reset_stats(self):
		"""stats that can change during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0