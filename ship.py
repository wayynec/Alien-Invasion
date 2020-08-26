#you
import pygame

class Ship():

	def __init__(self, screen):
		# initialize ship object and set its original position
		self.screen = screen


		# load the image for our ship
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# place the ship at bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		# put the ship at its place
		self.screen.blit(self.image, self.rect)