import shelve

class GameStats():
	"""Track various statistics"""

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.game_active = False
		self.reset_stats()

		# load high score (should never reset)
		high_score_file = shelve.open('high_score')
		self.high_score = high_score_file['high_score']
		high_score_file.close()

	def reset_stats(self):
		"""stats that can change during the game"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1