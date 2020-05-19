import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
	# initialize and create a screen object
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion Game")

	# create our ship on this screen
	ship = Ship(screen)

	# main loop for the game
	while True:

		# keeps monitoring keyboard and mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# it's always set to be filled with our background color and our ship
		screen.fill(game_settings.bg_color)
		ship.blitme()
		# display the latest screen
		pygame.display.flip()

run_game()