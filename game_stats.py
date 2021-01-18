class GameStats():
	"""class for points"""
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		self.game_active = False # if drops to zero: game over
		self.high_score = 0
		self.level = 1

	def reset_stats(self):
		"""initial all stats at the beginning"""
		self.ships_left = self.settings.ship_limit # eg ship life = 3
		self.score = 0
