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