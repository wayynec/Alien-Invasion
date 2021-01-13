import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" this class manages all the bullets shot out"""

	def __init__(self, settings, screen, ship):
		"""an instance of bullet at ship position"""
		super().__init__()
		self.screen = screen

		# create a bullet at 0,0 then move it to the correct position
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = ship.rect.centerx # align it with the ship
		self.rect.top = ship.rect.top

		# use float to more precisely indicate bullet's position
		self.y = float(self.rect.y)

		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor

	def update(self):
		"""move bullet up"""
		self.y -= self.speed_factor
		# update rect.y
		self.rect.y = self.y

	def draw_bullet(self):
		"""draw a bullet on screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)