import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""class alien, import Sprite so that it can be gouped"""

	def __init__(self, settings, screen):
		"""initialize alien and set its starting position"""
		super().__init__()
		self.settings = settings
		self.screen = screen

		# load alien image and set its rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# put it at the top left corner (0+width, 0+height)
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# accurate position with float
		self.x = float(self.rect.x)

	def blitme(self):
		"""put the alien image on the screen at defined position"""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""check if alien is at edge, if so return True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""update fleet to correct position"""
		self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
		self.rect.x = self.x