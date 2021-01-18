#you
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, settings, screen):
		super().__init__()
		# initialize ship object and set its original position
		self.screen = screen
		self.settings = settings

		# load the image for our ship, and make them rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# place the ship at bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# since centerx can only store integer, we need the exact float
		self.center = float(self.rect.centerx)

		# flag for pressing the key, ship keeps moving
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# if flag set, it will move by itself
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.settings.ship_speed_factor

		self.rect.centerx = self.center # update it back for next time

	def blitme(self):
		# put the ship at its place
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx