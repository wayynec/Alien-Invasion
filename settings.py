class Settings():
	# This class stores all settings in this game

	def __init__(self):
		# all initial static settings

		# screen
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# ship setting
		self.ship_limit = 3

		# bullet setting
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 255, 0, 0
		self.bullets_allowed = 3

		# alien setting
		self.fleet_drop_speed = 10 # speed going down

		# speed up factor with level
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""initialize all dynamic settings which chang as game proceeds"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		# fleet_direction: 1=right -1=left
		self.fleet_direction = 1
		# score setting
		self.alien_points = 50

	def increase_speed(self):
		"""increase speed every level"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.score_scale * self.alien_points)
