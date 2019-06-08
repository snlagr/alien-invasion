class Settings():
	"""Change your configuration here"""

	def __init__(self):
		"""Initialize"""
		# screen settings
		self.screen_width = 1300
		self.screen_height = 700
		self.bg_color = (230, 230, 230)

		# ships setting
		self.ship_speed_factor = 1.5

		# bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3