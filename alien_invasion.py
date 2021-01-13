import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
	# initialize the game and create a screen object
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion Game")

	# create our ship on background
	ship = Ship(game_settings, screen)
	# create a group for all bullets (inherited form Sprite superclass)
	bullets = Group()

	# main loop for the game
	while True:
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(game_settings, screen, ship, bullets)

		
		# print(len(bullets))
		

run_game()