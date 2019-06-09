class Settings():
	"""Change your configuration here"""

	def __init__(self):
		"""Initialize game's static settings"""
		# screen settings
		self.screen_width = 1300
		self.screen_height = 700
		self.bg_color = (230, 230, 230)

		# ships setting
		self.ship_limit = 3

		# bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# alien settings
		self.fleet_drop_speed = 10

		# how quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# 1 = right, -1 = left
		self.fleet_direction = 1

		# scoring
		self.alien_points = 50

	def increase_speed(self):
		"""increase speed settings"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale