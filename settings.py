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

		# bullet setting
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 0, 0
		self.bullets_allowed = 3
