import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	"""a class about score board information"""

	def __init__(self, settings, screen, stats):
		"""initialize score related properties"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.settings = settings
		self.stats = stats

		# font setting
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# prepare initial scoreboard
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""render text into image"""
		# round to tenth
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		# put the score on top right corner of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""display score on screen"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""render highest score into image"""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

		# put high score at the top center
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""render level into image"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

		# put level info under score on top right
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""remaining lives"""
		self.ships = Group()
		for ship_num in range(self.stats.ships_left):
			ship = Ship(self.settings, self.screen)
			ship.rect.x = 10 + ship_num * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
