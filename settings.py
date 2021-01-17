class Settings():
	# This class stores all settings in this game

	def __init__(self):
		# all initial settings

		# screen
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# ship setting
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		# bullet setting
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 0, 0
		self.bullets_allowed = 3

		# alien setting
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 100 # speed going down
		# fleet_direction: 1=right -1=left
		self.fleet_direction = 1
